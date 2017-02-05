
# microjson - Minimal JSON parser/emitter for use in standalone scripts.
# No warranty. Free to use/modify as you see fit. Trades speed for compactness.
# Send ideas, bugs, simplifications to http://github.com/phensley
# Copyright (c) 2010 Patrick Hensley <spaceboy@indirect.com>

# std
import math
import StringIO
import types


# the '_from_json_number' function returns either float or long.
__pychecker__ = 'no-returnvalues'

# character classes
WS = set([' ','\t','\r','\n','\b','\f'])
DIGITS = set([str(i) for i in range(0, 10)])
NUMSTART = DIGITS.union(['.','-','+'])
NUMCHARS = NUMSTART.union(['e','E'])
ESC_MAP = {'n':'\n','t':'\t','r':'\r','b':'\b','f':'\f'}
REV_ESC_MAP = dict([(_v,_k) for _k,_v in ESC_MAP.items()] + [('"','"')])

# error messages
E_BYTES = 'input string must be type str containing ASCII or UTF-8 bytes'
E_MALF = 'malformed JSON data'
E_TRUNC = 'truncated JSON data'
E_BOOL = 'expected boolean'
E_NULL = 'expected null'
E_LITEM = 'expected list item'
E_DKEY = 'expected key'
E_COLON = 'missing colon after key'
E_EMPTY = 'found empty string, not valid JSON data'
E_BADESC = 'bad escape character found'
E_UNSUPP = 'unsupported type "%s" cannot be JSON-encoded'
E_BADFLOAT = 'cannot emit floating point value "%s"'

NEG_INF = float('-inf')
POS_INF = float('inf')


class JSONError(Exception):
    def __init__(self, msg, stm=None, pos=0):
        if stm:
            msg += ' at position %d, "%s"' % (pos, repr(stm.substr(pos, 32)))
        Exception.__init__(self, msg)


class JSONStream(object):

    # no longer inherit directly from StringIO, since we only want to
    # expose the methods below and not allow direct access to the 
    # underlying stream.

    def __init__(self, data):
        self._stm = StringIO.StringIO(data)

    @property
    def pos(self):
        return self._stm.pos

    @property
    def len(self):
        return self._stm.len

    def getvalue(self):
        return self._stm.getvalue()

    def skipspaces(self):
        "post-cond: read pointer will be over first non-WS char"
        self._skip(lambda c: c not in WS)

    def _skip(self, stopcond):
        while True:
            c = self.peek()
            if stopcond(c) or c == '':
                break
            self.next()

    def next(self, size=1):
        return self._stm.read(size)

    def next_ord(self):
        return ord(self.next())

    def peek(self):
        if self.pos == self.len:
            return ''
        return self.getvalue()[self.pos]

    def substr(self, pos, length):
        return self.getvalue()[pos:pos+length]


def _decode_utf8(c0, stm):
    c0 = ord(c0)
    r = 0xFFFD      # unicode replacement character
    nc = stm.next_ord

    # 110yyyyy 10zzzzzz
    if (c0 & 0xE0) == 0xC0:
        r = ((c0 & 0x1F) << 6) + (nc() & 0x3F)

    # 1110xxxx 10yyyyyy 10zzzzzz
    elif (c0 & 0xF0) == 0xE0:
        r = ((c0 & 0x0F) << 12) + ((nc() & 0x3F) << 6) + (nc() & 0x3F)

    # 11110www 10xxxxxx 10yyyyyy 10zzzzzz
    elif (c0 & 0xF8) == 0xF0:
        r = ((c0 & 0x07) << 18) + ((nc() & 0x3F) << 12) + \
            ((nc() & 0x3F) << 6) + (nc() & 0x3F)
    return unichr(r)


def decode_escape(c, stm):
    # whitespace
    v = ESC_MAP.get(c, None)
    if v is not None:
        return v

    # plain character
    elif c != 'u':
        return c

    # decode unicode escape \u1234
    sv = 12
    r = 0
    for _ in range(0, 4):
        r |= int(stm.next(), 16) << sv
        sv -= 4
    return unichr(r)


def _from_json_string(stm):
    # skip over '"'
    stm.next()  
    r = []
    while True:
        c = stm.next()
        if c == '':
            raise JSONError(E_TRUNC, stm, stm.pos - 1)
        elif c == '\\':
            c = stm.next()
            r.append(decode_escape(c, stm))
        elif c == '"':
            return ''.join(r)
        elif c > '\x7f':
            r.append(_decode_utf8(c, stm))
        else:
            r.append(c)


def _from_json_fixed(stm, expected, value, errmsg):
    off = len(expected)
    pos = stm.pos
    if stm.substr(pos, off) == expected:
        stm.next(off)
        return value
    raise JSONError(errmsg, stm, pos)


def _from_json_number(stm):
    # Per rfc 4627 section 2.4 '0' and '0.1' are valid, but '01' and
    # '01.1' are not, presumably since this would be confused with an
    # octal number.  This rule is not enforced.
    is_float = 0
    saw_exp = 0
    pos = stm.pos
    while True:
        c = stm.peek()

        if c not in NUMCHARS:
            break
        elif c == '-' and not saw_exp:
            pass
        elif c in ('.','e','E'):
            is_float = 1
            if c in ('e','E'):
                saw_exp = 1
        stm.next() 

    s = stm.substr(pos, stm.pos - pos)
    if is_float:
        return float(s)
    return long(s)


def _from_json_list(stm):
    # skip over '['
    stm.next()
    result = []
    pos = stm.pos
    while True:
        stm.skipspaces()
        c = stm.peek()
        if c == '':
            raise JSONError(E_TRUNC, stm, pos)

        elif c == ']':
            stm.next()
            return result

        elif c == ',':
            stm.next()
            result.append(_from_json_raw(stm))
            continue

        elif not result:
            # first item
            result.append(_from_json_raw(stm))
            continue

        else:
            raise JSONError(E_MALF, stm, stm.pos)


def _from_json_dict(stm):
    # skip over '{'
    stm.next()
    result = {}
    expect_key = 0
    pos = stm.pos
    while True:
        stm.skipspaces()
        c = stm.peek()
        if c == '':
            raise JSONError(E_TRUNC, stm, pos)

        # end of dictionary, or next item
        if c in ('}',','):
            stm.next()
            if expect_key:
                raise JSONError(E_DKEY, stm, stm.pos)
            if c == '}':
                return result
            expect_key = 1
            continue

        # parse out a key/value pair
        elif c == '"':
            key = _from_json_string(stm)
            stm.skipspaces()
            c = stm.next()
            if c != ':':
                raise JSONError(E_COLON, stm, stm.pos)

            stm.skipspaces()
            val = _from_json_raw(stm)
            result[key] = val
            expect_key = 0
            continue

        # unexpected character in middle of dict
        raise JSONError(E_MALF, stm, stm.pos)


def _from_json_raw(stm):
    while True:
        stm.skipspaces()
        c = stm.peek()
        if c == '"': 
            return _from_json_string(stm)
        elif c == '{': 
            return _from_json_dict(stm)
        elif c == '[': 
            return _from_json_list(stm)
        elif c == 't':
            return _from_json_fixed(stm, 'true', True, E_BOOL)
        elif c == 'f':
            return _from_json_fixed(stm, 'false', False, E_BOOL)
        elif c == 'n': 
            return _from_json_fixed(stm, 'null', None, E_NULL)
        elif c in NUMSTART:
            return _from_json_number(stm)

        raise JSONError(E_MALF, stm, stm.pos)


def from_json(data):
    """
    Converts 'data' which is UTF-8 (or the 7-bit pure ASCII subset) into
    a Python representation.  You must pass bytes to this in a str type,
    not unicode.
    """
    if not isinstance(data, str):
        raise JSONError(E_BYTES)
    if not data:
        return None
    stm = JSONStream(data)
    return _from_json_raw(stm)


# JSON emitter

def _to_json_list(stm, lst):
    seen = 0
    stm.write('[')
    for elem in lst:
        if seen:
            stm.write(',')
        seen = 1
        _to_json_object(stm, elem)
    stm.write(']')


def _to_json_string(stm, buf):
    stm.write('"')
    for c in buf:
        nc = REV_ESC_MAP.get(c, None)
        if nc:
            stm.write('\\' + nc)
        elif ord(c) <= 0x7F:
            # force ascii
            stm.write(str(c))
        else:
            stm.write('\\u%04x' % ord(c))
    stm.write('"')


def _to_json_dict(stm, dct):
    seen = 0
    stm.write('{')
    for key in dct.keys():
        if seen:
            stm.write(',')
        seen = 1
        val = dct[key]
        if not type(key) in (types.StringType, types.UnicodeType):
            key = str(key)
        _to_json_string(stm, key)
        stm.write(':')
        _to_json_object(stm, val)
    stm.write('}')


def _to_json_object(stm, obj):
    if isinstance(obj, (types.ListType, types.TupleType)):
        _to_json_list(stm, obj)
    elif isinstance(obj, types.BooleanType):
        if obj:
            stm.write('true')
        else:
            stm.write('false')
    elif isinstance(obj, types.FloatType):
        # this raises an error for NaN, -inf and inf values
        if not (NEG_INF < obj < POS_INF):
            raise JSONError(E_BADFLOAT % obj)
        stm.write("%s" % obj)
    elif isinstance(obj, (types.IntType, types.LongType)):
        stm.write("%d" % obj)
    elif isinstance(obj, types.NoneType):
        stm.write('null')
    elif isinstance(obj, (types.StringType, types.UnicodeType)):
        _to_json_string(stm, obj)
    elif hasattr(obj, 'keys') and hasattr(obj, '__getitem__'):
        _to_json_dict(stm, obj)
    # fall back to implicit string conversion.
    elif hasattr(obj, '__unicode__'):
        _to_json_string(stm, obj.__unicode__())
    elif hasattr(obj, '__str__'):
        _to_json_string(stm, obj.__str__())
    else:
        raise JSONError(E_UNSUPP % type(obj))


def to_json(obj):
    """
    Converts 'obj' to an ASCII JSON string representation.
    """
    stm = StringIO.StringIO('')
    _to_json_object(stm, obj)
    return stm.getvalue()


decode = from_json
encode = to_json

