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
        r = f'<{self.name} '
        for a in self.attributes:
            r += f'{repr(a)} '
        r += '>'
        for c in self.children:
            r += f' {repr(c)} '
        r += f'<\{self.name}>'
        return r    
    
class AttributeNode:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return f'''Attribute Name: {self.name}
Value: {self.value}'''

    def __repr__(self):
        return f'{self.name}={self.value}'

class TextNode:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f'''Content: {self.content}'''
    
    def __repr__(self):
        return self.content