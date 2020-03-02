"""
Flyweight is a structural design pattern that lets you fit more objects 
into the available amount of RAM by sharing common parts of state between 
multiple objects instead of keeping all of the data in each object.

When object has mutable and immutable fields and the immutable fields
take RAM, when having many objects, the immutable fields are making the
objects take too much RAM.
The idea is to have the immutable fields separately (single instance of them),
the the objects will just use reference, not store the field on themselves
"""


class Projectile:

    def __init__(self, x, y, speed, vector):
        self.x = x
        self.y = y
        self.speed = speed
        self.vector = vector
    
    def __repr__(self):
        return 'x %s, y %s, speed %s, vector %s' % (
            self.x, self.y, self.speed, self.vector)


class Spaceship:
    """
    single enemy "boss" spaceship
    
    Example: instead of having the bullet.png sprite stored in each bullet,
    will have single instance of it, so no matter how many bullets we have
    the sprite won't consume more RAM
    """
    
    def __init__(self):
        self.rocket_sprite = 'rocket.png'
        self.bullet_sprite = 'bullet.png'
        self.bullets = []
        self.rockets = []
        
    def draw(self):
        self.draw_bullets()
        self.draw_rockets()
    
    def draw_bullets(self):
        for b in self.bullets:
            self.draw_projectile(b, self.bullet_sprite)
    
    def draw_rockets(self):
        for r in self.rockets:
            self.draw_projectile(r, self.rocket_sprite)
            
    def draw_projectile(self, projectile, sprite):
        print('draw -> %s, %s' % (sprite, projectile))
        

def run():
    b1 = Projectile(5, 4, 10, [])
    b2 = Projectile(6, 6, 14, [])
    r1 = Projectile(25, 55, 50, [])
    spaceship = Spaceship()
    spaceship.bullets = [b1, b2]
    spaceship.rockets = [r1]
    spaceship.draw()


if __name__ == '__main__':
    run()
