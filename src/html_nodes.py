class TagNode:
    def __init__(self, name, attributes=None, text=None, children=None, parent=None):
        self.name = name
        self.attributes = attributes or []
        self.text = text or ''
        self.children = children or []
        self.parent = parent

    def __str__(self):
        attributes_str = ', '.join(str(attr) for attr in self.attributes)
        children_str = '\n'.join(str(child) for child in self.children)
        parent_name = self.parent.name if self.parent else None
        return f'''Tag Name: {self.name}\nAttributes: [{attributes_str}]\nText: {self.text}\nParent: {parent_name}\nChildren:\n{children_str}'''
    
    def __repr__(self):
        r = f'<{self.name} '
        for a in self.attributes:
            r += f'{repr(a)} '
        r = r[:-1] + '>'    
        r += self.text
        for c in self.children:
            r += f'{repr(c)}'
        r += f'</{self.name}>'
        return r    
    
    def add_child(self, child):
        if child:
            self.children.append(child)
            child.parent = self
    
class AttributeNode:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return f'''Attribute Name: {self.name} - Attribute Value: {self.value}'''

    def __repr__(self):
        return f'{self.name}={self.value}'
