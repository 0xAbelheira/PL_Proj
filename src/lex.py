import ply.lex as lex

states = (
    ('tag', 'exclusive'),
    ('attribute', 'exclusive')
)

tokens = [
    'TAG_NAME',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'COMMA',
    'TEXT_CONTENT',
    'ATTRIBUTE_NAME',
    'ATTRIBUTE_VALUE',
    'INDENT',
    'OUTDENT'
]

def t_TAG_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    lexer.push_state('tag')
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

def t_attribute_RPAREN(t):
    r'\)'
    lexer.pop_state()
    return t

def t_attribute_EQUALS(t):
    r'='
    return t

def t_attribute_COMMA(t):
    r','
    return t

def t_tag_TEXT_CONTENT(t):
    r'[^# \t\n]+'
    t.lexer.pop_state()
    return t

t_ANY_ignore = ' '

indent_level = 0

# Newline handling
def t_ANY_newline(t):
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
def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
