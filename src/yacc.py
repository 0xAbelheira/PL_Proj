import ply.yacc as yacc
from html_nodes import *

from lex import tokens

prev_lineno = 0

def p_tag(p):
    '''
    tag : TAG_NAME LPAREN attributes RPAREN TEXT_CONTENT INDENT tag
        | TAG_NAME LPAREN attributes RPAREN INDENT tag
        | TAG_NAME TEXT_CONTENT INDENT tag
        | TAG_NAME INDENT tag
        | TAG_NAME LPAREN attributes RPAREN TEXT_CONTENT OUTDENT tag
        | TAG_NAME LPAREN attributes RPAREN OUTDENT tag
        | TAG_NAME TEXT_CONTENT OUTDENT tag
        | TAG_NAME OUTDENT tag
        | TAG_NAME LPAREN attributes RPAREN TEXT_CONTENT OUTDENT
        | TAG_NAME LPAREN attributes RPAREN OUTDENT
        | TAG_NAME TEXT_CONTENT OUTDENT
        | TAG_NAME OUTDENT
    '''
    if len(p) == 8 and p[6] == 'INDENT':
        p[0] = TagNode(p[1], p[3], [TextNode(p[5])].append(p[7]))
    elif len(p) == 8 and p[6] == 'OUTDENT':
        pass
    elif len(p) == 7 and p[5] == 'INDENT':
        p[0] = TagNode(p[1], p[3], [p[7]])
    elif len(p) == 7 and p[5] == 'OUTDENT':
        pass
    elif len(p) == 5 and p[3] == 'INDENT':
        p[0] = TagNode(p[1], [], [TextNode(p[2])].append(p[4]))
    elif len(p) == 5 and p[3] == 'OUTDENT':
        p[0] =  TagNode(p[1], [], p[3])
    elif len(p) == 4 and p[2] == 'INDENT':
        pass
    elif len(p) == 4 and p[2] == 'OUTDENT':
        pass
    elif len(p) == 7 and p[6] == 'OUTDENT':
        pass
    elif len(p) == 6 and p[5] == 'OUTDENT':
        pass
    elif len(p) == 4 and p[3] == 'OUTDENT':
        pass
    elif len(p) == 3 and p[2] == 'OUTDENT':
        pass

    # if len(p) == 6:
    #     p[0] = TagNode(p[1], p[3], [TextNode(p[5])])
    # elif len(p) == 5:
    #     p[0] = TagNode(p[1], p[3])
    # elif len(p) == 2:
    #     p[0] = TagNode(p[1])


def p_attributes(p):
    '''
    attributes : attribute COMMA attributes
               | attribute
    '''

    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_attribute(p):
    '''
    attribute : ATTRIBUTE_NAME EQUALS ATTRIBUTE_VALUE
              | attribute_empty
    '''
    if len(p) == 4:
        p[0] = AttributeNode(p[1], p[3])

def p_attribute_empty(p):
    '''
    attribute_empty :
    '''
    p[0] = []

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

with open("../test.pug", 'r') as f:
    code = f.read()
    print("a comecar")
    print(repr(parser.parse(code, debug=True)))