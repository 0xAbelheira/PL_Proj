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

class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, node, identation_level):
        print(self.stack)
        print(node)
        if len(self.stack) == 0:
            self.stack.append((node, identation_level))

        else:
            while (self.stack[-1][1] > identation_level):
               child = self.stack.pop()
               node.add_child(child[0])
               if len(self.stack) == 0:
                   break
            self.stack.append((node, identation_level))
        print(self.stack, '\n\n')

    def __str__(self):
        sb = ''
        for i in range(len(self.stack)-1, -1, -1):
            sb += f'node: {repr(self.stack[i][0])} dent_level: {self.stack[i][1]}\n'
        return sb