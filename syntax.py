import ply.yacc as yacc


from lexer import tokens, reserved, states, lexer


def p_doctype(p):
    '''
    doctype : DOCTYPE
    '''
    print(p[1])
    p[0] = "<!DOCTYPE html>"

def p_tag(p):
    '''
    tag : TAG
    '''
    print(p[1])
    p[0] = '<' + p[1] + '/>'

# Error handling
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()
parser.lexer = lexer

# Parse the Pug code and generate the HTML
with open("test_files/test.pug", 'r') as f:
    code = f.read()
    print(parser.parse(code))
