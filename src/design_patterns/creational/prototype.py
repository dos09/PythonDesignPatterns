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
        return copy.deepcopy(self.type_humanoid_map.get(humanoid_type))

    
class Humanoid:

    def __init__(self):
        self.name = 'N/A'
        self.stat = {
            'hp': 10,
            'kills': 0
        }
    
    def __copy__(self):
        obj = self.__class__(self.name)
        obj.stat = copy.copy(self.stat)
        return obj
        
    def __deepcopy__(self, memo):
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
    orc1.stat['hp'] = 11
    orc2.name = 'orc2'
    orc1.show()
    orc2.show()
