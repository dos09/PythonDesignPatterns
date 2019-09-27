"""
Facade = interface that hides complexity
Example: 
    class that provides the client fewer/simpler
    methods to use. This class uses other class(es)
    and the idea is to simplify the usage of this/those class(es)
"""


class Shape:

    def draw(self):
        raise NotImplementedError()

    
class Circle(Shape):
    
    def draw(self):
        print('draw circle')

        
class Rectangle(Shape):
    
    def draw(self):
        print('draw rectangle')

        
class ShapeDrawer:
    
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle() 
    
    def draw_circle(self):
        self.circle.draw()
    
    def draw_rectangle(self):
        self.rectangle.draw()


if __name__ == '__main__':
    shape_drawer = ShapeDrawer()
    shape_drawer.draw_circle()
    shape_drawer.draw_rectangle()
