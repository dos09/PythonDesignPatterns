"""
Goal: decoupling

Description 1 (confusing):
Makes the implementation of concrete classes (Circle)
independent from the implementation of "interface implementing classes" 
(RedCircleDrawAPI, GreenCircleDrawAPI)

Description 2:
    Shape  -> uses  Color
    /   \            / \          
Circle Rectangle   Red Green

    When having shape and need to add color to it, instead of having
    sub-classes like RedCircle, RedRectangle, the Shape class will use
    Color object (composition)
"""


class DrawAPI:

    def draw_circle(self, x, y, radius):
        print('default circle: x %s, y %s, radius %s' % (x, y, radius))
        # raise NotImplementedError()
    
    def draw_rectangle(self, x, y, a, b):
        print('default rectangle: x %s, y %s, a %s, b %s' % (x, y, a, b))
        # raise NotImplementedError()

    
class RedCircleDrawAPI(DrawAPI):

    def draw_circle(self, x, y, radius):
        print('red circle: x %s, y %s, radius %s' % (x, y, radius))


class GreenCircleDrawAPI(DrawAPI):

    def draw_circle(self, x, y, radius):
        print('green circle: x %s, y %s, radius %s' % (x, y, radius))

        
class Shape():
    
    def __init__(self, draw_api):
        self.draw_api = draw_api
        
    def draw_circle(self, x, y, radius):
        self.draw_api.draw_circle(x, y, radius)
        
    def draw_rectangle(self, x, y, a, b):
        self.draw_api.draw_rectangle(x, y, a, b)


class Circle(Shape):

    def __init__(self, x, y, radius, draw_api=None):
        super().__init__(draw_api or DrawAPI())
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self):
        super().draw_circle(self.x, self.y, self.radius)


if __name__ == '__main__':   
    red_circle = Circle(5, 10, 12, RedCircleDrawAPI())
    green_circle = Circle(1, 2, 10, GreenCircleDrawAPI())
    banana_circle = Circle(19, 91, 21)
    red_circle.draw()
    green_circle.draw()
    banana_circle.draw()
