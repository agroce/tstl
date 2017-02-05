import math
import StringIO
import types
__pychecker__ = 'no-returnvalues'
WS = set([' ', '\t', '\r', '\n', '\x08', '\x0c'])
DIGITS = set([str(i) for i in range(0, 10)])
NUMSTART = DIGITS.union(['.', '-', '+'])
NUMCHARS = NUMSTART.union(['e', 'E'])
ESC_MAP = {'n': '\n', 't': '\t', 'r': '\r', 'b': '\x08', 'f': '\x0c'}
REV_ESC_MAP = dict([(_v, _k) for (_k, _v) in ESC_MAP.items()] + [('"', '"')])
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
        'post-cond: read pointer will be over first non-WS char'
        self._skip(lambda c: (c not in WS))

    def _skip(self, stopcond):
        while True:
            c = self.peek()
            if (stopcond(c) or (c == '')):
                break
            self.next()

    def next(self, size=1):
        return self._stm.read(size)

    def next_ord(self):
        return ord(self.next())

    def peek(self):
        if (self.pos == self.len):
            return ''
        return self.getvalue()[self.pos]

    def substr(self, pos, length):
        return self.getvalue()[pos:pos + length]

def _decode_utf8(c0, stm):
    c0 = ord(c0)
    r = 65533
    nc = stm.next_ord
    if (c0 & 224 == 192):
        r = c0 & 31 << 6 + nc() & 63
    elif (c0 & 240 == 224):
        r = c0 & 15 << 12 + nc() // 63 << 6 + nc() & 63
    elif (c0 & 248 == 240):
        r = c0 & 7 << 18 + nc() & 63 << 12 + nc() & 63 << 6 + nc() & 63
    return unichr(r)

def decode_escape(c, stm):
    v = ESC_MAP.get(c, None)
    if (v is not None):
        return v
    elif (c != 'u'):
        return c
    sv = 12
    r = 0
    for _ in range(0, 4):
        r |= int(stm.next(), 16) << sv
        sv -= 4
    return unichr(r)

def _from_json_string(stm):
    stm.next()
    r = []
    while True:
        c = stm.next()
        if (c == ''):
            raiseJSONError(E_TRUNC, stm, stm.pos - 1)
        elif (c == '\\'):
            c = stm.next()
            r.append(decode_escape(c, stm))
        elif (c == '"'):
            return ''.join(r)
        elif (c > '\x7f'):
            r.append(_decode_utf8(c, stm))
        else:
            r.append(c)

def _from_json_fixed(stm, expected, value, errmsg):
    off = len(expected)
    pos = stm.pos
    if (stm.substr(pos, off) == expected):
        stm.next(off)
        return value
    raiseJSONError(errmsg, stm, pos)

def _from_json_number(stm):
    is_float = 0
    saw_exp = 0
    pos = stm.pos
    while True:
        c = stm.peek()
        if (c not in NUMCHARS):
            break
        elif ((c == '-') and (not saw_exp)):
            pass
        elif (c in ('.', 'e', 'E')):
            is_float = 1
            if (c in ('e', 'E')):
                saw_exp = 1
        stm.next()
    s = stm.substr(pos, stm.pos - pos)
    if is_float:
        return float(s)
    return long(s)

def _from_json_list(stm):
    stm.next()
    result = []
    pos = stm.pos
    while True:
        stm.skipspaces()
        c = stm.peek()
        if (c == ''):
            raiseJSONError(E_TRUNC, stm, pos)
        elif (c == ']'):
            stm.next()
            return result
        elif (c == ','):
            stm.next()
            result.append(_from_json_raw(stm))
            continue
        elif (not result):
            result.append(_from_json_raw(stm))
            continue
        else:
            raiseJSONError(E_MALF, stm, stm.pos)

def _from_json_dict(stm):
    stm.next()
    result = {}
    expect_key = 0
    pos = stm.pos
    while True:
        stm.skipspaces()
        c = stm.peek()
        if (c == ''):
            raiseJSONError(E_TRUNC, stm, pos)
        if (c in ('}', ',')):
            stm.next()
            if expect_key:
                raiseJSONError(E_DKEY, stm, stm.pos)
            if (c == '}'):
                return result
            expect_key = 1
            continue
        elif (c == '"'):
            key = _from_json_string(stm)
            stm.skipspaces()
            c = stm.next()
            if (c != ':'):
                raiseJSONError(E_COLON, stm, stm.pos)
            stm.skipspaces()
            val = _from_json_raw(stm)
            result[key] = val
            expect_key = 0
            continue
        raiseJSONError(E_MALF, stm, stm.pos)

def _from_json_raw(stm):
    while True:
        stm.skipspaces()
        c = stm.peek()
        if (c == '"'):
            return _from_json_string(stm)
        elif (c == '{'):
            return _from_json_dict(stm)
        elif (c == '['):
            return _from_json_list(stm)
        elif (c == 't'):
            return _from_json_fixed(stm, 'true', True, E_BOOL)
        elif (c == 'f'):
            return _from_json_fixed(stm, 'false', False, E_BOOL)
        elif (c == 'n'):
            return _from_json_fixed(stm, 'null', None, E_NULL)
        elif (c in NUMSTART):
            return _from_json_number(stm)
        raiseJSONError(E_MALF, stm, stm.pos)

def from_json(data):
    "\n    Converts 'data' which is UTF-8 (or the 7-bit pure ASCII subset) into\n    a Python representation.  You must pass bytes to this in a str type,\n    not unicode.\n    "
    if (not isinstance(data, str)):
        raiseJSONError(E_BYTES)
    if (not data):
        return None
    stm = JSONStream(data)
    return _from_json_raw(stm)

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
        elif (ord(c) <= 127):
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
        if (not (type(key) in (types.StringType, types.UnicodeType))):
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
        if (not (NEG_INF < obj < POS_INF)):
            raiseJSONError(E_BADFLOAT % obj)
        stm.write('%s' % obj)
    elif isinstance(obj, (types.IntType, types.LongType)):
        stm.write('%d' % obj)
    elif isinstance(obj, types.NoneType):
        stm.write('null')
    elif isinstance(obj, (types.StringType, types.UnicodeType)):
        _to_json_string(stm, obj)
    elif (hasattr(obj, 'keys') and hasattr(obj, '__getitem__')):
        _to_json_dict(stm, obj)
    elif hasattr(obj, '__unicode__'):
        _to_json_string(stm, obj.__unicode__())
    elif hasattr(obj, '__str__'):
        _to_json_string(stm, obj.__str__())
    else:
        raiseJSONError(E_UNSUPP % type(obj))

def to_json(obj):
    "\n    Converts 'obj' to an ASCII JSON string representation.\n    "
    stm = StringIO.StringIO('')
    _to_json_object(stm, obj)
    return stm.getvalue()
decode = from_json
encode = to_json