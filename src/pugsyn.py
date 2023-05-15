import ply.yacc as yacc

from puglex import tokens

class TagNode:
    def __init__(self, name, attributes=None, children=None):
        self.name = name
        self.attributes = attributes or []
        self.children = children or []

    def __str__(self):
        return f'''Tag Name: {self.name}
Attributes: {self.attributes}
Children: {self.children}'''

    def __repr__(self):
        return f''' '''
    
class AttributeNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'''Attribute Name: {self.name}
Value: {self.value}'''

class TextNode:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f'''Content: {self.content}'''

"""
def p_doctype(p):
    '''
    doctype : DOCTYPE
    '''
    p[0] = "<!DOCTYPE html>"
    pug_ast["doctype"] = p[0]
    print(pug_ast)
"""


def p_tag(p):
    '''
    tag : TAG_NAME LPAREN attributes RPAREN tag_children
        | TAG_NAME tag_children
    '''
    p[0] = TagNode(p[1], p[2], p[3])

    
def p_attributes(p):
    '''
    attributes : attribute COMMA attributes 
               | attribute  

    '''
    p[0] = [AttributeNode(p[1])] + p[3]

def p_attribute(p):
    '''
    attribute : ATTRIBUTE_NAME EQUALS ATTRIBUTE_VALUE 
              | attribute_empty
    '''
    p[0] = AttributeNode(p[1], p[3])


def p_attribute_empty(p):
    'attribute_empty : '
    p[0] = []

def p_tag_children(p):
    'tag_children : tag tag_children'
    p[0] = [p[1]] + p[2]

def p_tag_children_text(p):
    'tag_children : TEXT_CONTENT tag_children'
    p[0] = [TextNode(p[1])] + p[2]

def p_tag_children_empty(p):
    'tag_children : '
    p[0] = []


# Error handling
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()

# Parse the Pug code and generate the HTML
with open("../test.pug", 'r') as f:
    code = f.read()
    print(parser.parse(code, debug=False))


