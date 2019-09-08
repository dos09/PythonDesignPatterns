
    
class Circle:

    def draw(self):
        print('draw -> circle')


class Rectangle:

    def draw(self):
        print('draw -> rectangle')


class ShapeFactory:
    
    @staticmethod
    def get_shape(shape_name):
        if isinstance(shape_name, str):
            shape_name = shape_name.lower()
            if shape_name == 'circle':
                return Circle()
            
            if shape_name == 'rectangle':
                return Rectangle()
        
        return None


if __name__ == '__main__':
    c = ShapeFactory.get_shape('circle')
    c.draw()
    r = ShapeFactory.get_shape('rectangle')
    r.draw()
