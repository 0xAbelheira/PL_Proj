import ply.yacc as yacc
from html_nodes import *

from lex import tokens

prev_lineno = 0
dent_level = 0

stack = Stack()

def p_line(p):
    '''
    line : dent tag line
         | tag line
         | dent_tag_aux
    '''
    if len(p) == 4:
        stack.push(p[2], p[1])
    elif len(p) == 3:
        stack.push(p[1], 0)
        p[0] = stack.stack[0][0]

def p_dent_tag_aux(p):
    '''
    dent_tag_aux : dent tag
    '''
    stack.push(p[2], p[1])


def p_line_empty(p):
    '''
    line_empty : 
    '''
    p[0] = None

def p_dent(p):
    '''
    dent : indent
         | outdent
         | nodent
    '''
    p[0] = p[1]

def p_indent(p):
    '''
    indent : INDENT
    '''
    global dent_level 
    dent_level += 1
    p[0] = dent_level

def p_outdent(p):
    '''
    outdent : OUTDENT
    '''
    global dent_level
    p[0] = p[1] // 4

def p_nodent(p):
    '''
    nodent : NODENT
    '''
    global dent_level
    p[0] = dent_level

def p_tag(p):
    '''
    tag : TAG_NAME inside_tag 
        | div_tag
    '''
    if len(p) == 3:
        p[0] = TagNode(name=p[1], attributes=p[2][0], text=p[2][1])
    else:
        p[0] = TagNode(name="div", attributes=p[1][0], text=p[1][1])
    
def p_div_tag(p):
    '''
    div_tag : inside_tag
    '''
    p[0] = p[1]

def p_inside_tag(p):
    '''
    inside_tag : attributes_aux text
    '''
    p[0] = [p[1], p[2]]



def p_attributes_aux(p):
    '''
    attributes_aux : attributes
                   | attribute_empty
    '''
    p[0] = p[1]


def p_tag_empty(p):
    '''
    tag_empty :
    '''
    p[0] = []

def p_attributes(p):
    '''
    attributes : LPAREN attributes_list RPAREN special_attribute
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

def p_attributes_list(p):
    '''
    attributes_list : attribute COMMA attributes_list
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
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_text_emtpy(p):
    '''
    text_empty :
    '''
    p[0] = ''

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

with open("test.pug", 'r') as f:
    code = f.read()
    output = parser.parse(code, debug=True)
    print(repr(output), sep='\n')

with open("test.html", 'w') as f:
    f.write(repr(output))
