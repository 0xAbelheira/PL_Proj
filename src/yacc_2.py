import ply.yacc as yacc
from html_nodes import *

from lex import tokens

prev_lineno = 0
dent_level = 0

def p_pug(p):
    '''
    pug : tag_list
    '''
    p[0] = TagNode(name='yoo', children=p[1])

def p_tag_list(p):
    '''
    tag_list : tag 
             | tag_list tag
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_tag_tag(p):
    '''
    tag : TAG_NAME
        | TAG_NAME INDENT tag_list OUTDENT
    '''
    if len(p) == 2:
        p[0] = TagNode(name=p[1])
    else:
        p[0] = TagNode(name=p[1], children=p[3])

def p_tag_attributes(p):
    '''
    tag : TAG_NAME attributes
        | TAG_NAME attributes INDENT tag_list OUTDENT
    '''
    if len(p) == 3:
        p[0] = TagNode(name=p[1], attributes=p[2])
    else:
        p[0] = TagNode(name=p[1], attributes=p[2], children=[p[4]])

def p_tag_text(p):
    '''
    tag : TAG_NAME text
        | TAG_NAME text INDENT tag_list OUTDENT
    '''
    if len(p) == 3:
        p[0] = TagNode(name=p[1], text=p[2])
    else:
        p[0] = TagNode(name=p[1], text=p[2], children=[p[4]])

def p_tag_attributes_text(p):
    '''
    tag : TAG_NAME attributes text
        | TAG_NAME attributes text INDENT tag_list OUTDENT
    '''
    if len(p) == 3:
        p[0] = TagNode(name=p[1], attributes=p[2], text=[p[3]])
    else:
        p[0] = TagNode(name=p[1], attributes=p[2], text=p[3], children=[p[4]])



def p_tag_empty(p):
    '''
    tag_empty :
    '''
    p[0] = None

def p_attributes(p):
    '''
    attributes : LPAREN attribute_list RPAREN special_attribute
               | special_attribute attributes
               | special_attribute attribute_empty
               | attribute_empty
    '''
    if len(p) == 5:
        p[0] = p[2] + p[4]
    if len(p) == 3:
        p[0] = p[1] + p[2]
    if len(p) == 2:
        p[0] = p[1]

def p_attribute_list(p):
    '''
    attribute_list : attribute COMMA attribute_list
                    | attribute
    '''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    if len(p) == 2:
        p[0] = [p[1]]

def p_attribute(p):
    '''
    attribute : ATTRIBUTE_NAME EQUALS ATTRIBUTE_VALUE
              | attribute_empty
    '''
    if len(p) == 4:
        p[0] = AttributeNode(p[1], p[3])
    if len(p) == 2:
        p[0] = p[1] 

def p_attribute_empty(p):
    '''
    attribute_empty :
    '''
    p[0] = []

def p_special_attribute(p):
    '''
    special_attribute : class_attribute
                      | id_attribute
    '''
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

def p_text(p):
    '''
    text : SPACE TEXT
         | text_empty
    '''
    p[0] = p[2]

def p_text_emtpy(p):
    '''
    text_empty :
    '''
    p[0] = ''

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

with open("../test.pug", 'r') as f:
    code = f.read()
    output = parser.parse(code, debug=True)
    print(output, repr(output), sep='\n')

with open("../test.html", 'w') as f:
    f.write(repr(output))
