"""
Cache used objects, if object X is needed,
check in cache, if there -> use it, else create it,
cache it and use it
"""
import random


class Circle:
    
    def __init__(self, color):
        self.color = color.lower()
    
    def draw(self):
        print('drawing %s circle' % self.color)


class CirclesCache:
    
    MAX_CACHE_SIZE = 100
        
    def __init__(self):
        self.data = {}
        
    def get_circle(self, color):
        color = color.lower()
        circle = self.data.get(color)
        if not circle:
            print(' * Creating %s circle' % color)
            circle = Circle(color)
            if len(self.data) >= CirclesCache.MAX_CACHE_SIZE:
                self.data.clear()

            self.data[color] = circle
        
        return circle


def run():
    colors = ['red', 'green', 'blue', 'yellow']
    cache = CirclesCache()
    for _ in range(6):
        circle = cache.get_circle(random.choice(colors))
        circle.draw()


if __name__ == '__main__':
    run()
