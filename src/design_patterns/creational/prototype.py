"""
When the initialization of object X is heavy/time-consuming,
instead of initializing new instance every time, initialize it once,
cache it and when instance is needed, just copy from the cache.

Keeping objects in cache is not needed. Object can be copied and passed
to method when the original object should not be changed
Example:
    obj = ClassX()
    # need to have clone method in ClassX
    do_sth_that_will_change_obj(obj.clone())
    # or
    # need to override __copy__ and/or __deepcopy__ in ClassX
    do_sth_that_will_change_obj(copy.deepcopy(obj))
"""
import copy


class Cache:
    
    def __init__(self):
        self.type_humanoid_map = {}
    
    def load(self):
        '''
        some time consuming and/or processing heavy
        initializing of objects, which are then cached 
        (so it's better to copy such object
        instead of initialize it when needed, 
        for example the initializing needs
        lots of database operations)
        '''
        self.type_humanoid_map = {
            'orc': Orc(),
            'human': Human()
        }

    def get(self, humanoid_type):
        return copy.deepcopy(self.type_humanoid_map[humanoid_type])

    
class Humanoid:

    def __init__(self):
        self.name = 'N/A'
        self.stat = {
            'hp': 100,
            'kills': 0
        }
    
    def __copy__(self):
#         print('copy')
        obj = self.__class__()
        obj.name = self.name
        obj.stat = copy.copy(self.stat)
        return obj
        
    def __deepcopy__(self, memo):
#         print('deepcopy')
        obj = self.__class__()
        for attr_name, value in self.__dict__.items():
            setattr(obj, attr_name, copy.deepcopy(value, memo))
        
        return obj
    
    def show(self):
        print('name: %s, stat: %s' % (self.name, self.stat))


class Orc(Humanoid):

    def __init__(self):
        super().__init__()


class Human(Humanoid):

    def __init__(self):
        super().__init__()

    
if __name__ == '__main__':
    cache = Cache()
    cache.load()
    orc1 = cache.get('orc')
    orc2 = cache.get('orc')
    orc1.show()
    orc2.show()
    orc1.name = 'orc1'
    orc1.stat['hp'] = 111
    orc2.name = 'orc2'
    orc1.show()
    orc2.show()
