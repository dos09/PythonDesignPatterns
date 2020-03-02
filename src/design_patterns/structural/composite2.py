"""
Also known as: Object Tree
Composite is a structural design pattern that lets you compose objects into 
tree structures and then work with these structures as if they were individual 
objects.

use case: products and boxes. Can have a box with products and boxes,
and these boxes can have other products and boxes, ...

Calculating the price of box with nested boxes and products can
be achieved with this pattern
"""


class Component:
    
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        
    def add(self, component):
        self.children.append(component)
        component.parent = self
        
    def remove(self, component):
        self.children.remove(component)
        component.parent = None
        
#     def show(self, indent=''):
#         print('%s%s' % (indent, self.name))
#         for child in self.children:
#             child.show(indent + '    ')
    def show(self, indent=0):

        def build_indent_prefix():
            if not indent:
                return ''
            
            return ' ' * indent + '|--'
        
        print('%s%s' % (build_indent_prefix(), self.name))
        if not self.children:
            print('')
            return
        
        for child in self.children:
            child.show(indent + 3)
     

def run():
    """
                |-> A_1_2
        /-> A_1 |-> A_1_1 -> A_1_1_1
    root
        \-> B_1 |-> B_1_1
                |-> B_1_2
    """
    root = Component('root')
    a_1 = Component('A_1')
    a_1_1 = Component('A_1_1')
    a_1_2 = Component('A_1_2')
    a_1_1_1 = Component('A_1_1_1')
    b_1 = Component('B_1')
    b_1_1 = Component('B_1_1')
    b_1_2 = Component('B_1_2')
    
    a_1.add(a_1_1)
    a_1.add(a_1_2)
    a_1_1.add(a_1_1_1)
    
    b_1.add(b_1_1)
    b_1.add(b_1_2)
    
    root.add(a_1)
    root.add(b_1)
    
    root.show()

    
if __name__ == '__main__':
    run()
