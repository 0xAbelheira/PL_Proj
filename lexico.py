import ply.lex as lex


states = (
    ('intag', 'exclusive'),

)

reserved = {
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
    'audio': 'AUDIO'
}

'''    embed
    object
    iframe
    form
    input
    button
    select
    option
    textarea
    label
    fieldset
    legend
    br
    hr
    div
    span
    table
    tr
    td, th
    caption
    col, colgroup
    tbody, thead, tfoot
    small
    strong
    em
    code
    pre
    blockquote
    q
    abbr
    acronym
    cite
    dfn
    kbd
    samp
    var
    sub
    sup
    time
    mark
    ruby, rp, rt
    bdo
    wbr'''


# List of token names
tokens = [
    'TAG',   
    'PLAIN_TEXT',
    'ATTRIBUTE'
] + list(reserved.values())



def t_TAG(t):
   r'[a-z]+'
   t.type = reserved.get(t.value, 'TAG')
   t.lexer.begin('intag')
   return t

# TENHO DE VER O Q TA MAL AQUI
def t_intag_ATTRIBUTE(t):
    r'\((.*?)\)'
    return t

def t_intag_PLAIN_TEXT(t):
   r'[^#\.\n]+'
   t.lexer.begin('INITIAL')
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
t_ignore = ' \t'


# Handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

with open("test_files/test.pug", 'r') as f:
    str = f.readline()
    lexer.input(str)

while tok := lexer.token():
    print(tok)

