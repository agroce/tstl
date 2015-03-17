#!/usr/bin/env python

"""
Help module to parse a simple XML buffer and store it as a read-only (mostly)
dictionary-type object (MyXml). This dictionary can hold other dictionaries,
nodes-lists, or leaf nodes. Access to the nodes is by using attributes.

>>> xml = parse("<Foo><Bar>Val</Bar></Foo>")
>>> xml.Foo.Bar == "Val"
True
>>> xml.Foo.Bar
<Bar>Val</Bar>

I don't like to use the built in Python DOM parsers for simple XML data, but
this module is good only for simple XML! No name-spaces, CDATA and other fancy
features are supported.

There are three factory functions, "parse", "parse_file" and "parse_object".

- parse takes an XML string and builds MyXml object from it.

- parse_file takes a file name reads it and do the same.

Both functions take an optional list of tags names from the beginning of the
XML data, to ignore.

- parse_object takes a complex python object (of dictionaries, sequences and
scalars) and creates MyXml object from it.

It is possible, but not convenient, to construct an XML trees using this module.

Usage Examples:

>>> xml = parse('''
... <?xml bla bla bla>
... <!-- Comment -->
... <Main>
...	  <Text>One Two &amp; Three</Text>
...	  <List>
...		<!-- This is a list of items -->
...	    <Item aaa="bbb" ></Item>
...	    <Item ccc = "ab&#43;c" />
...	    <Item>Bla Bla Bla</Item>
...	  </List>
...	  <BoolNum num="3.5" bool="Yes">No</BoolNum>
...   <Double><Double>Value</Double></Double>
... </Main>
... ''')

- An XML node is an attribute of the MyXml object

>>> xml.Main.Text
<Text>One Two &amp; Three</Text>

- And also

>>> xml.Main.Text == "One Two & Three"
True

>>> xml.Main.Text.value == "One Two &amp; Three"
True

There is also a way to access a node with "nd_" prefix (so we can access
python reserved words), this will also return EMPY_NODE if the node doesn't
exists.

>>> xml.nd_Main.nd_Text
<Text>One Two &amp; Three</Text>

- A node can be looked at as a list with one item

>>> xml.Main.Double.Double[0] is xml.Main.Double.Double
True

- Nodes Lists are regular lists
>>> len(xml.Main.List.Item)
3
>>> unicode(xml.Main.List.Item[2])
u'Bla Bla Bla'

- MyXml object is a dictionary

>>> xml["Main"]["Text"] == xml.Main["Text"]
True
>>> xml.Main.get("Text") == xml["Main"].Text
True

- There is also a very simple XPath-like method

>>> xml.xpath("Main/List/Item")[2]
<Item>Bla Bla Bla</Item>

- Attributes can be accessed with an "at_" prefix

>>> xml.Main.List.Item[1].at_ccc
u'ab&#43;c'

- Access the attributes dictionary with "at_dict"

>>> xml.Main.List.Item[0].at_dict["aaa"]
u'bbb'

- Every value can be looked at as a number and a boolean

>>> xml.Main.BoolNum.boolean
False

- Also attribute can be looked at as booleans or numbers

>>> xml.Main.BoolNum.at_num.number * 2
7.0
>>> xml.xpath("Main/BoolNum").at_bool.boolean
True

- But if the value is not a number or boolean (yes, no, true, false, 1, 0) the
- return value is None

>>> xml.Main.List.Item[0].at_aaa.number

- "get" and "xpath" return an empty node by default, so we can still use the
-	number/boolean attributes.

>>> bool(xml.get("foo").boolean)
False

>>> xml.xpath("Main/foo").number is None
True

- Printing MyXml objects keeps the original order and adds indentation.
- The indentation is not thread safe though.

>>> print xml.Main.List
<List>
  <Item aaa="bbb" />
  <Item ccc="ab&#43;c" />
  <Item>Bla Bla Bla</Item>
</List>

- Constructing MyXml object from a python complex object:

>>> xml = parse_object({
... "foo1": "bar",
... "foo2": ["bar1", "bar2", "bar3"],
... "foo3": {"bar": "foo"},
... "foo4": 5
... }, "Main")	# "Main" is the name of the top most node

>>> xml.xpath("Main/foo4").number
5

- The names of the nodes that hold a sequence items, are the type name of the
- sequence (list, tuple, set, generator).

>>> xml.xpath("Main/foo2/list")[1] == "bar2"
True

- Finally - not very useful - but you can modify MyXml object

>>> add_returns_self = xml.add(MyNode("bar5", "foo5"))	# MyNode(value, name)
>>> xml.foo5.at_dict["attr"] = "attr value"
>>> xml.xpath("Main/foo5").at_attr == "attr value"
True

One can also use the other built in dictionary and list methods, but this is not
recommended

>>> xml		# Here the order is not preserved because of the python dictionary
<Main>
  <foo4>5</foo4>
  <foo1>bar</foo1>
  <foo2>
    <list>bar1</list>
    <list>bar2</list>
    <list>bar3</list>
  </foo2>
  <foo3>
    <bar>foo</bar>
  </foo3>
  <foo5 attr="attr value">bar5</foo5>
</Main>

Please note that this module is not efficient in parsing large XML buffers. It
uses string slicing heavily.

Erez Bibi

Please send comments and questions to
erezbibi AT users DOT sourceforge DOT net
"""

import re
import htmlentitydefs
from types import GeneratorType

INDENT = "  "

class MyXmlError(Exception): pass

class MyValue(unicode):
	"""
	Holds an end value, this can be Node value or attribute value.
	This is a unicode object that adds a "number" and "boolean" attributes.
	"""
	def __new__(cls, value=None, *args, **kw):
		if value is None:
			value = ''
		return unicode.__new__(cls, value)


	@property
	def number(self):
		""" Try to return the value as a number or None """
		try:
			return int(self)
		except:
			try:
				return float(self)
			except:
				return None

	@property
	def boolean(self):
		""" Try to return the value as a boolean or None.
		It will work is the value is true, yes, 1, false, no or 0.
		"""
		val = self.lower()
		if val in ("true", "yes", "1"): return True
		if val in ("false", "no", "0"): return False
		return None

	@property
	def value(self):
	    """ Return the raw text as an ASCII string """
	    return str(self)

EMPTY_VALUE = MyValue()


class MyXml(object):
	"""
	Base element for Node, NodesList and NodesDict.
	Has name and attributes (as a regular dictionary)
	"""

	_indent = 0

	def __init__(self, name, attr=None):
		assert isinstance(name, str), "name must be a string"
		assert attr is None or  isinstance(attr, dict), \
			"attr must be a dictionary (or missing)"
		self._name = name
		self._attr = attr

	@property
	def node_name(self):
		return self._name

	@property
	def at_dict(self):
		""" If attr is None I create it here """
		if self._attr is None:
			self._attr = {}
		return self._attr

	def __getattr__(self, name):
		""" If asking for attribute (starts with at_) return it or EMPTY_VALUE """
		if not self._attr is None and name.startswith("at_"):
			return self._attr.get(name[3:], EMPTY_VALUE)
		raise AttributeError, ("%s is not an attribute of MyXml" % name)

	def as_list(self):
		"""
		Return this node as a NodesList, if it is not already a NodesList, it
		Creates one and insert 'self' into it.
		Doesn't change the object
		One can access a MyNode object as a list with one item,
		so I don't really need the function as global function anymore.
		"""
		if isinstance(self, MyNodesList):
			return self
		lst = MyNodesList(self._name)
		lst.add(self)
		return lst

	def __len__(self):
		""" I put it here so bool (...) will always work. """
		return 0

class MyNode(MyValue, MyXml):
	"""
	Represents a leaf node in the XML tree. Can hold a value.
	This is an immutable value (but not it's attributes dictionary).
	"""
	def __init__(self, value='', name='', attr=None):
		# value goes to MyValue __new__
		MyXml.__init__(self, name, attr)

	def __unicode__(self):
		""" Unquote the string (if needed) before returning it """
		return _unquote_html(self)

	def __repr__(self):
		""" return XML tag as a string """
		ret = INDENT * MyXml._indent + '<' + self._name
		if self._attr:
			ret += ' ' + ' '.join ('%s="%s"' % (key, val) for key, val in \
				self._attr.items())
		if self:
			ret += ">%s</%s>" % (self.value, self._name)
		else:
			ret += " />"
		return ret

	def __eq__(self, obj):
		""" Can compare objects or unicode values """
		if isinstance(obj, self.__class__):
			# Compare the entire object (name, attr, value)
			return hash(self) == hash(obj)
		# Compare only values
		return unicode(self) == unicode(obj)

	def __ne__(self, obj):
		return not self.__eq__(obj)

	def __getitem__(self, key):
		""" This function is so we can look at this node as one item list """
		if not isinstance(key, int):
			raise TypeError, "Cannot slice a NodesList"
		if key != 0:
			raise IndexError
		return self

	def add(self, node):
		""" Not implemented in leaf nodes """
		raise NotImplementedError, "Leaf node is immutable"


# Construct an Empty Node
EMPTY_NODE = MyNode()

class MyNodesList(list, MyXml):
	""" A list of nodes (all with the same name). """
	def __init__(self, name, attr=None, value=None):
		""" Optional value can be any sequence, the items will be added to this
		MyNodesList object.
		"""
		MyXml.__init__(self, name, attr)
		if value:
			for item in value:
				self.add(_object2xml(name, item))

	def __repr__(self):
		return '\n'.join(itm.__repr__() for itm in self)

	def add(self, node):
		""" Add a new node to the list """
		assert isinstance(node, MyXml), "node must be MyXml object"
		assert node.node_name == self.node_name, \
			"NodesList accepts only nodes with same name"
		self.append(node)
		return self

class MyNodesDict(dict, MyXml):
	""" Represents a group of node as a dictionary. This is the top most node of
	every XML tree.
	"""
	def __init__(self, name='', attr=None, xml=None, value=None):
		""" Optional xml can be an XML string to parse.
		Optional value can be a mapping object, the items will be added to this
		MyNodesDict object. xml and value are mutual exclusive.
		"""
		MyXml.__init__(self, name, attr)
		self._order = []	# To preserve the original insertion order
		if xml:
			_text2dict(self, xml)
		elif value:
			for key, val in value.iteritems():
				self.add(_object2xml(key, val))

	def __getattr__(self, name):
		""" Access XML nodes as instance attributes
		There is also a way to access a node with "nd_" prefix (so we can access
		python reserved words), this will also return EMPY_NODE if the node
		doesn't exists.
		"""
		if self.has_key(name):
			return self[name]
		if name.startswith("nd_"):
			return self.get(name[3:], EMPTY_NODE)
		return MyXml.__getattr__(self, name)

	def __setattr__(self, name, val):
		if name and name[0] == '_':
			return MyXml.__setattr__(self, name, val)
		raise NotImplementedError, "Nodes-Dict attributes are immutable"

	def __repr__(self):
		""" Return the dictionary data as XML string """
		MyXml._indent += 1
		values = '\n'.join (itm.__repr__() for itm in self.ordered_values())
		MyXml._indent -= 1
		# If the name of the dict is empty string, this is the top node
		# and it will print just the dict content
		if not self._name: return values
		ret = INDENT * MyXml._indent + '<' + self._name
		if self._attr:
			ret += ' ' + ' '.join ('%s="%s"' % (key, val) for key, val in \
				self._attr.items ())
		ret += ">\n%s\n%s</%s>" % (values, INDENT * MyXml._indent, self._name)
		return ret

	def __getitem__(self, key):
		""" This logic is so we can look at this dictionary as one item list """
		if isinstance(key, int):
			if key == 0:
				return self
			else:
				raise IndexError
		return dict.__getitem__(self, key)

	def get(self, key, default=EMPTY_NODE):
		""" Default value is EMPTY_NODE """
		return dict.get(self, key, default)

	def add(self, node):
		""" Add a node to the dictionary. If a node with the same name is
		already in, it will create a NodesList (or just append to a NodesList)
		"""
		assert isinstance(node, MyXml), "node must be MyXml object"
		#assert node.node_name, "new node must have a name"
		if not node.node_name:
		    for sub_node in node.values():
		        self.add(sub_node)
		elif node.node_name in self:
			tmp = self[node.node_name].as_list()
			tmp.add(node)
			self[node.node_name] = tmp
		else:
			self._order.append(node.node_name)
			self[node.node_name] = node
		return self

	def xpath(self, path):
		""" Simple XPath style query on a NodesDict. If the path doesn't exists
		it will return an EMPTY_NODE.
		"""
		dic = self
		path = path.split('/')
		# Deal with the top name if exists
		if dic.node_name:
			if dic.node_name != path[0]:
				return EMPTY_NODE
			path = path[1:]
		for itm in path:
			if not isinstance(dic, MyNodesDict): return EMPTY_NODE
			dic = dic.get(itm)
			if not dic: return dic
		return dic

	def ordered_values(self):
		""" Like values but return the list in the original order """
		return [self[key] for key in self._order]


## Functions to build the MyXml object ##


# regular expression to separate tags attributes
_re_inner_tag = re.compile("(([\w\.:]+)(\s*=\s*\"(.*?)\")?)", re.M | re.S | re.I)

# unquote HTML
_re_unquote = re.compile("&(#?)(.+?);")


def _convert_entity(m):
    """Convert an HTML entity into normal string (ISO-8859-1)
	From: http://groups.google.com/group/comp.lang.python/browse_thread/thread/7f96723282376f8c/"""
    if m.group(1)=='#':
        try:
            return chr(int(m.group(2)))
        except ValueError:
            return '&#%s;' % m.group(2)
    try:
        return htmlentitydefs.entitydefs[m.group(2)]
    except KeyError:
        return '&%s;' % m.group(2)

def _unquote_html (string):
	"""Convert a HTML quoted string into normal string (ISO-8859-1).
	Works with &#XX; and with &nbsp; &gt; etc.
	From: http://groups.google.com/group/comp.lang.python/browse_thread/thread/7f96723282376f8c/"""
	if not string: return string
	return _re_unquote.sub(_convert_entity, string)

def _get_inner_tag(text):
	""" Gets a string of the inner text of a tag (<...>)
	Returns a tuple of the tag name, tag attributes dictionary (or None), and if
	the tag is containing tag (<tag>...</tag>)
	"""
	if not text[0].isalpha():	# Not a tag for us
		return None, None, None
	contains = not text.rstrip().endswith('/')
	lst = _re_inner_tag.findall(text)
	if not lst:
		raise MyXmlError, "Cannot understand this tag format: %s..." % text[:min(10, len(text))]
	name = lst[0][1]
	if lst[1:]:
		attr = dict((atr[1], MyValue(atr[3])) for atr in lst[1:])
	else:
		attr = None
	return name, attr, contains

def _get1item(text):
	""" Get an XML text and returns a tuple that holds the next tag in the text.
	Returns tuple of tag name, tag attributes, tag striped content (may by
	None) and the length of this tag (in the input text)
	"""
	i = text.find('>')
	if not text or text[0] != '<' or i == -1:
		raise MyXmlError, "Cannot understand this format: %s..." % text[:min(20, len(text))]
	name, attr, contains = _get_inner_tag(text[1:i])
	if contains:
		# Find the correct closing tag
		j = counter = 0
		for mtch in re.finditer(
		"</?%s(?:\s+[^<]*?[^/])?>" % name, text, re.S|re.I):
			if mtch.group()[1] == '/': counter -= 1
			else: counter += 1
			j = mtch.start()
			if counter == 0: break
		if not j or counter != 0:
			raise MyXmlError, "Cannot understand this format: Cannot find </%s>" % name
		content = text[i+1:j].strip()
		length = j + len(name) + 3
	else:
		content = None
		length = i + 1
	return name, attr, content, length

def _text2dict(dic, text):
	""" Get a MyNodesDict and an XML text, and put the XML nodes content in the
	dictionary. This is a recursive function, it finds a tag (node), if the
	content of this tag is an XML string (starts with '<'), it creates a new
	NodesDict from the tag, and call itself with the new dict and the content,
	if the content is plain text or None it create a simple Node. Then it
	inserts the new tag to the NodesDict it received as argument and continue to
	the next tag.
	Returns the received MyNodesDict
	"""
	text = text.lstrip()
	while text:
		name, attr, content, length = _get1item(text)
		text = text[length:].lstrip()
		if name:
			if not content or content[0] != '<':
				item = MyNode(content, name, attr)
			else:
				item = MyNodesDict(name, attr)
				_text2dict(item, content)
			dic.add(item)
	return dic

def _object2xml(name, obj):
	""" Convert a dictionary, sequence, scalar or combination of the above to
	MyXml object. Works with the constructors of the three MyXml classes.
	"""
	if isinstance(obj, dict):
		return MyNodesDict(name, value=obj)
	elif isinstance(obj, list) or isinstance(obj, tuple) or \
	isinstance(obj, set) or isinstance(obj, GeneratorType):
		return MyNodesDict(name).add(MyNodesList(type(obj).__name__, value=obj))
	else:
		return MyNode(obj, name)


_re_comment = re.compile("<!--.*?-->", re.M | re.S | re.I)

def _remove_comments(text):
	""" Strip the text from <!-- comments --> """
	return _re_comment.sub(' ', text)

def _remove_titles(text, ignore):
	""" Old Implementation
	This function just removes wrappers tags in the beginning of the XML text.
	Parameters:
		text - The XML text as string.
		ignore - List of tag to remove (ignore). This list has to be of
			only wrappers tags and in the order they appear in the XML text.
			It can be list, tuple or string (if only removing one tag).
	Returns:
		(String) The XML text without the wrappers tags.
	"""
	# This is not a completely correct implementation, but it is not very useful
	# function either
	if not isinstance (ignore, list) and not isinstance (ignore, tuple):
		ignore = [ignore]
	for x in ignore:
		text = text.strip()
		if text.startswith("<" + x):
			text = text[text.find(">")+1:]
		i = text.rfind("</" + x + ">")
		if i != -1:
			text = text[:i]
	return text


## Public Factory Functions ##


def parse(text, ignore=None):
	""" Parse an XML text and return the top MyNodesDict
	"""
	# Drop the comments and title(s).
	text = _remove_comments(text)
	if ignore:
		text = _remove_titles(text, ignore)
	# Parse the XML document.
	return MyNodesDict(xml=text)

def parse_file(filename, ignore=None):
	""" Open a file and parse it """
	with open(filename, "rb") as fl:
		dic = parse(fl.read(), ignore)
	return dic

def parse_object(obj, name=''):
	""" Parse a python object of dictionaries, sequences, scalars and
	combination of these, to MyXml dictionary.
	"""
	return _object2xml(name, obj)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

	print "Test Passed"

