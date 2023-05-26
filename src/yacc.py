import ply.yacc as yacc
from html_nodes import *

from lex import tokens

prev_lineno = 0

def p_tag(p):
    ''' 
    tag : TAG_NAME attributes text INDENT tag 
        | TAG_NAME attributes INDENT tag
        | TAG_NAME text INDENT tag
        | TAG_NAME INDENT tag
        | TAG_NAME attributes text
        | TAG_NAME text
        | tag_emtpy
    '''
    if len(p) == 6:
        p[0] = TagNode(p[1], p[2], [TextNode(p[3])] + [p[5]])
    if len(p) == 5:
        p[0] = TagNode(p[1], p[2], [p[5]])
    if len(p) == 5:
        p[0] = TagNode(p[1], [], [TextNode(p[2])] + [p[4]])
    if len(p) == 4:
        p[0] = TagNode(p[1], p[2], [TextNode(p[3])])
    if len(p) == 4:
        p[0] = TagNode(p[1], [], [p[3]])
    if len(p) == 3:
        p[0] = TagNode(p[1], [], [TextNode(p[2])])
    if len(p) == 2:
        p[0] = TagNode(p[1])

def p_text(p):
    '''
    text : SPACE TEXT
    '''
    p[0] = p[2]

def p_attributes(p):
    '''
    attributes : LPAREN attributes_list RPAREN
               | class_attribute
               | id_attribute
    '''
    if len(p) == 4:
        p[0] = p[2]
    if len(p) == 2:
        p[0] = p[1]

def p_class_attribute(p):
    '''
    class_attribute : DOT SPECIAL_ATTRIBUTE id_attribute
                    | class_attribute_empty
    '''
    if len(p) == 4:
        p[0] = [AttributeNode('class', f'"{p[2]}"')] + p[3]
    if len(p) == 2:
        p[0] = p[1]

def p_id_attribute(p):
    '''
    id_attribute : HASHTAG SPECIAL_ATTRIBUTE class_attribute
                 | id_attribute_empty
    '''
    if len(p) == 4:
        p[0] = [AttributeNode('id', f'"{p[2]}"')] + p[3]
    if len(p) == 2:
        p[0] = p[1]

def p_class_attribute_emtpy(p):
    '''
    class_attribute_empty :
    '''
    p[0] = []

def p_id_attribute_empty(p):
    '''
    id_attribute_empty :
    '''
    p[0] = []

def p_tag_emtpy(p):
    '''
    tag_emtpy :
    '''
    p[0] = []

def p_attributes_list(p):
    '''
    attributes_list : attribute COMMA attributes_list
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
    print(repr(parser.parse(code, debug=True)))