import ply.lex as lex

states = (
    ('tag', 'exclusive'),
    ('attribute', 'exclusive'),
    ('special', 'exclusive'),
    ('multitext', 'exclusive')
)

tokens = [
    'TAG_NAME',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'COMMA',
    'TEXT',
    'ATTRIBUTE_NAME',
    'ATTRIBUTE_VALUE',
    'INDENT',
    'OUTDENT',
    'NODENT',
    'DOT',
    'HASHTAG',
    'SPACE',
    'SPECIAL_ATTRIBUTE'
]

def t_TAG_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    lexer.push_state('tag')
    return t

# Newline handling
def t_ANY_newline(t):
    r'\n[ \t]*'
    global indent_level
    t.lexer.lineno += 1
    i = len(t.value) - 1
    t.lexer.begin('INITIAL')

    if (i == indent_level):
        t.type = 'NODENT'
        t.value = i
        return t
    elif (t.value[-1] != '\n'):
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
"""
def t_SPECIAL_DOT(t):
    r'\.\n'
    lexer.push_state('multitext')
    return t

def t_multitext_MULTITEXT(t):
    r'(\ +)([^\n]+)'
"""

def t_DOT(t):
    r'\.'
    lexer.push_state('tag')
    lexer.push_state('special')
    return t

def t_HASHTAG(t):
    r'\#'
    lexer.push_state('tag')
    lexer.push_state('special')
    return t

def t_tag_DOT(t):
    r'\.'
    lexer.push_state('special')
    return t

def t_tag_HASHTAG(t):
    r'\#'
    lexer.push_state('special')
    return t

def t_special_SPECIAL_ATTRIBUTE(t):
    r'[^\ \.\#\(\)]+'
    lexer.pop_state()
    return t

def t_tag_LPAREN(t):
    r'\('
    lexer.push_state('attribute')
    return t

def t_attribute_ATTRIBUTE_NAME(t):
    r'[\w\-]+'
    return t

def t_attribute_ATTRIBUTE_VALUE(t):
    r'".*?"'
    return t

def t_attribute_EQUALS(t):
    r'='
    return t

def t_attribute_COMMA(t):
    r','
    return t

def t_attribute_RPAREN(t):
    r'\)'
    lexer.pop_state()
    return t

def t_tag_TEXT(t):
    r'[^\ ][^#\n]+'
    t.lexer.pop_state()
    return t

def t_tag_SPACE(t):
    r'\ '
    return t

t_ANY_ignore = ''

indent_level = 0



# Error handling
def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

'''
with open("../test.pug", 'r') as f:
    lines = ""
    for line in f.readlines():
        lines += line
    lexer.input(lines)
    for tok in lexer:
        print(tok)
'''