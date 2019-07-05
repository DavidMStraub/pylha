import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

def numval(token):
    """Return the numerical value of token.value if it is a number"""
    if token.type == 'INTEGER':
        return int(token.value)
    elif token.type == 'FLOAT':
        return float(token.value)
    else:
        return token.value

_tokens = [
        ('FLOAT',  r'(?:[\+\-])?((?:\d+\.\d*|\.\d+)(?:[eEdD][\+\-]\d+)?|\d+(?:[eEdD][\+\-]\d+))(?!\.)'),
        ('INTEGER',  r'(?:[\+\-])?\d+(?!\.)'),
        ('BLOCK',      r'^[a-z]+'),
        ('NEWLINE', r'\n'),
        ('SKIP',    r'[ \t]+'),
        ('COMMENT',r'#.*'),
        ('WORD',r'[\w\=\.]+'),
        ('OTHER',r'[^#]*'),
    ]

def tokenize(code):
    """Tokenize the string `code`"""
    tok_regex = '|'.join('(?P<{}>{})'.format(*pair) for pair in _tokens)
    tok_regex = re.compile(tok_regex, re.IGNORECASE|re.M)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP' or value=='':
            pass
        else:
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)

class ParseError(Exception):
    pass

def parse(tokens, comments=False):
    """Parse the token list into a hierarchical data structure.

    If `comments` is set to True, line comments will be treated as
    normal string values rather than ignored."""
    d = collections.OrderedDict()
    prev_line = 0
    blockname = None
    blockline = None
    for token in tokens:
        if token.type == 'COMMENT' and (not comments or token.line != prev_line):
            continue  # ignore comments on new line or when comments is False
        elif token.type == 'BLOCK':
            block = token
            blockline = token.line
            blocktype = token.value.upper()
            blockname = None
            if blocktype not in d:
                d[blocktype] = collections.OrderedDict()
        elif token.line == blockline:
            if blockname is None:
                blockname = token.value
                d[blocktype][blockname] = collections.defaultdict(list)
            else:
                d[blocktype][blockname]['info'].append(numval(token))
        elif token.line != prev_line:
            if blockname is None:
                if token.type == 'COMMENT':
                    continue
                else:
                    raise ParseError("Found value outside block!")
            d[blocktype][blockname]['values'].append([numval(token)])
        else:
            if blockname is None:
                raise ParseError("Found value outside block!")
            d[blocktype][blockname]['values'][-1].append(numval(token))
        prev_line = token.line
    return d

def load(stream, comments=False):
    """Parse the LHA document and produce the corresponding Python object.
    Accepts a string or a file-like object.

    If `comments` is set to True, line comments will be treated as
    normal string values rather than ignored."""
    if isinstance(stream, str):
        string = stream
    else:
        string = stream.read()
    tokens = tokenize(string)
    return parse(tokens, comments=comments)
