import ply.lex as lex


states = (
    ('intag', 'exclusive'),
)

reserved = {
    # Reserved words for tags
    'doctype': 'DOCTYPE',
    'html': 'HTML',
    'head': 'HEAD',
    'title': 'TITLE',
    'meta': 'META',
    'link': 'LINK',
    'style': 'STYLE',
    'script': 'SCRIPT',
    'body': 'BODY',
    'article': 'ARTICLE',
    'section': 'SECTION',
    'aside': 'ASIDE',
    'header': 'HEADER',
    'footer': 'FOOTER',
    'nav': 'NAV',
    'h1': 'H1',
    'h2': 'H2',
    'h3': 'H3',
    'h4': 'H4',
    'h5': 'H5',
    'h6': 'H6',
    'p': 'P',
    'ul': 'UL',
    'ol': 'OL',
    'li': 'LI',
    'a': 'A',
    'img': 'IMG',
    'video': 'VIDEO',
    ':audio': 'AUDIO',
    'object': 'OBJECT',
    'iframe': 'IFRAME',
    'form': 'FORM',
    'embed': 'EMBED',
    'input': 'INPUT',
    'button': 'BUTTON',
    'select': 'SELECT',
    'option': 'OPTION',
    'textarea': 'TEXTAREA',
    'label': 'LABEL',
    'fieldset': 'FIELDSET',
    'legend': 'LEGEND',
    'br': 'BR',
    'hr': 'HR',
    'div': 'DIV',
    'span': 'SPAN',
    'table': 'TABLE',
    'tr': 'TR',
    'td': 'TD',
    'th': 'TH',
    'caption': 'CAPTION',
    'col': 'COL',
    'colgroup': 'COLGROUP',
    'tbody': 'TBODY',
    'thead': 'THEAD',
    'tfoot': 'TFOOT',
    'small': 'SMALL',
    'strong': 'STRONG', 
    'em': 'EM',
    'code': 'CODE',
    'pre': 'PRE',
    'blockquote': 'BLOCKQUOTE',
    'q': 'Q',
    'abbr': 'ABBR',
    'acronym': 'ACRONYM',
    'cite': 'CITE',
    'dfn': 'DFN',
    'kbd': 'KBD',
    'samp': 'SAMP',
    'var': 'VAR',
    'sub': 'SUB', 
    'sup': 'SUP',
    'time': 'TIME',
    'mark': 'MARK',
    'ruby': 'RUBY',
    'rp': 'RP',
    'rt': 'RT',
    'bdo': 'BDO',
    'wbr': 'WBR',
    'optgroup': 'OPTGROUP',
    'datalist': 'DATALIST',
    'output': 'OUTPUT',
    'progress': 'PROGRESS',
    'meter': 'METER',
    'b': 'B'
}

# List of token names
tokens = [
    'INDENT', 
    'TAG',   
    'PLAIN_TEXT',
    'ATTRIBUTE'
] + list(reserved.values())


indent_value = 0

def t_ANY_INDENT(t):
    r'(\ {2})+'
    indent_value_aux = len(t.value)
    if(indent_value_aux == indent_value + 2):
        return t

def t_ANY_TAG(t):
   r'[a-z0-9]+'
   t.type = reserved.get(t.value, 'TAG')
   t.lexer.push_state('intag')
   return t


# TENHO DE VER O Q TA MAL AQUI
def t_intag_ATTRIBUTE(t):
    r'\((.*?)\)'
    return t


def t_intag_PLAIN_TEXT(t):
   r'[^#\.\n]+'
   return t





#t_INDENT = r''
#t_OUTDENT = r''
#t_NEWLINE = r'\n'
#t_DOCTYPE = r''
#t_ID = r''
#t_CLASS = r''
#t_ATTRIBUTE = r'\(([\w-]+)(?:=(["'])(.*?)\2)?\)'
#t_INTERPOLATED_CODE = r'#\{.*\}' # e.g. msg="not my inside voice" in: p This is #{msg.toUpperCase()} ; out: <p>This is NOT MY INSIDE VOICE</p>
#t_BUFFERED_COMMENT = r'\/\/.*' # single line buffered comment e.g. in: // this is a comment that will show for HTML readers ;  out: <!-- this is a comment that will show for HTML readers -->
#t_UNBUFFERED_COMMENT = r'\/\/\-.*' # single line unbuffered comment e.g. in: //- this is a comment that will not show for HTML readers ; out: 

# Ignored characters (whitespace)
t_ANY_ignore = '\t'


# Handle newlines
def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# Error handling
def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

with open("test_files/test.pug", 'r') as f:
    str = f.read()  
    lexer.input(str)  

while tok := lexer.token():
    print(tok)

