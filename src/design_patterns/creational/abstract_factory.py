class AbstractFactory:
    
    @staticmethod
    def get_factory(factory):
        if isinstance(factory, str):
            factory = factory.lower()
            if factory == 'horde':
                return HordeFactory()
            
            if factory == 'alliance':
                return AllianceFactory()
            
        return None


class HordeFactory:

    @staticmethod
    def get_warrior(name):
        if isinstance(name, str):
            name = name.lower()
            if name == 'orc':
                return Orc()
            
            if name == 'tauren':
                return Tauren()
        
        return None


class AllianceFactory:

    @staticmethod
    def get_warrior(name):
        if isinstance(name, str):
            name = name.lower()
            if name == 'human':
                return Human()
        
        return None


class Orc:

    def attack(self):
        print('orc -> attack')

        
class Tauren:

    def attack(self):
        print('tauren -> attack')

        
class Human:

    def attack(self):
        print('human -> attack')


if __name__ == '__main__':
    horde_factory = AbstractFactory.get_factory('horde')
    alliance_factory = AbstractFactory.get_factory('alliance')
    
    orc = horde_factory.get_warrior('orc')    
    tauren = horde_factory.get_warrior('tauren')    
    human = alliance_factory.get_warrior('human')

    orc.attack()
    tauren.attack()
    human.attack()
    
