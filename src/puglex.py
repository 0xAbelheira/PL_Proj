import ply.lex as lex

states = (
    #('doctype', 'exclusive'),
    #('code', 'exclusive'),
    #('tag', 'exclusive'),
    #('class', 'exclusive'),
    #('attribute', 'exclusive'),
    #('id', 'exclusive'),
    #('interpolation', 'exclusive'),
    #('comment', 'exclusive'),
    #('icomment', 'exclusive'),
)    

reserved = {
    # Reserved words for tags
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
    #'DOCTYPE',
    #'INDENT',
    #'OUTDENT',
    'TAG_NAME',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'COMMA',
    'ATTRIBUTE_NAME',
    'ATTRIBUTE_VALUE',
    'TEXT_CONTENT'  ]
    #'CLASS', 
    #'ATTRIBUTE',
    #'PLAIN_TEXT',
    #'DOT',
    #'LPAREN',
    #'RPAREN',
    #'HASHTAG', 
    #'ID_LITERAL', 
    #'BEGIN_INTERPOLATION', 
    #'INTERPOLATED_CODE', 
    #'END_INTERPOLATION', 
    #'DASH',
    #'CODE',
    #'DOUBLE_SLASH_DASH',
    #'DOUBLE_SLASH',
    #'UNBUFFERED_COMMENT',
    #'BUFFERED_COMMENT'
#] + list(reserved.values())

"""
def t_DOCTYPE(t):
    r'doctype\ html'
    #t.lexer.begin('doctype')
    return t
"""

def t_TAG_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    #t.type = reserved.get(t.value, 'TAG')
    #t.lexer.begin('tag')
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_ATTRIBUTE_NAME(t):
    r'[\w\-]+'
    return t

def t_ATTRIBUTE_VALUE(t):
    r'".*?"'
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_EQUALS(t):
    r'='
    return t

def t_COMMA(t):
    r','
    return t

"""
def t_ANY_DOUBLE_SLASH_DASH(t):
    r'\/\/\-'
    t.lexer.begin('icomment')
    return t

def t_ANY_DOUBLE_SLASH(t):
    r'\/\/'
    t.lexer.begin('comment')
    return t

def t_doctype_tag_DASH(t):
    r'\-'
    t.lexer.begin('code')
    return t

def t_tag_class_LPAREN(t):
    r'\('
    t.lexer.begin('attribute')
    return t

def t_tag_PLAIN_TEXT(t):
   r'[^#\.\n]+'
   t.value = t.value[1:]
   return t

def t_code_CODE(t):
    r'.+'
    t.lexer.begin('tag')
    return t

def t_attribute_RPAREN(t): 
    r'\)'
    t.lexer.begin('tag')
    return t

def t_tag_DOT(t):
    r'\.'
    t.lexer.begin('class')
    return t

def t_class_CLASS(t):
    r'[a-z0-9\-]+'
    t.lexer.begin('tag')
    return t

def t_attribute_ATTRIBUTE(t):
    r'[^\(\)]+'
    return t

def t_tag_BEGIN_INTERPOLATION(t):
    r'\#\{'
    t.lexer.begin('interpolation')
    return t

def t_tag_HASHTAG(t):
    r'\#'
    t.lexer.begin('id')
    return t

def t_id_ID_LITERAL(t):
    r'[^#\.\n]+'
    t.lexer.begin('tag')
    return t

def t_interpolation_INTERPOLATED_CODE(t):
    r'[^\{\}]+'
    return t

def t_interpolation_END_INTERPOLATION(t):
    r'\}'
    t.lexer.begin('tag')
    return t

def t_icomment_UNBUFFERED_COMMENT(t):
    r'.+'
    t.lexer.begin('tag')
    return t

def t_comment_BUFFERED_COMMENT(t):
    r'.+'
    t.lexer.begin('tag')
    return t
"""
# Ignored characters (whitespace)
t_ignore = ' '




indent_level = 0

# Newline handling
def t_newline(t):
    r'\n[ \t]*'
    global indent_level
    t.lexer.lineno += 1
    i = len(t.value) - 1
    if (t.value[-1] != '\n') and (i != indent_level):
        if i > indent_level:
            t.type = 'INDENT'
            t.value = i
            indent_level = i
        elif i < indent_level:
            t.type = 'OUTDENT'
            t.value = i
            indent_level = i
        return t
    else:
        pass

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

with open("../test.pug", 'r') as f:
    str = f.read()  
    lexer.input(str)  

while tok := lexer.token():
    print(tok)

