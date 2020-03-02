"""
Singleton is a creational design pattern that lets you ensure that a class 
has only one instance
"""

class Singleton():
    
    OBJ = None
    
    def __init__(self):
        if Singleton.OBJ is not None:
            raise Exception('Singleton usage only')
    
    @staticmethod
    def get_instance():
        if Singleton.OBJ is None:
            Singleton.OBJ = Singleton()
        
        return Singleton.OBJ
    
    def talk(self):
        print('I am banana')


if __name__ == '__main__':
    obj = Singleton.get_instance()
    obj.talk()
