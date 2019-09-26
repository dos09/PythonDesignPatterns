class Warrior:
    
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        raise NotImplementedError()


class Orc(Warrior):
    
    def attack(self):
        print('the orc %s attacks' % self.name)


class Tauren(Warrior):
    
    def attack(self):
        print('the tauren %s attacks' % self.name)
        
        
class FartingDecorator: # FartingWarrior
    
    def __init__(self, warrior):
        self.warrior = warrior
        
    def attack(self):
        self.warrior.attack()
        self._fart()
    
    def _fart(self):
        print('%s is farting out loud' % self.warrior.name)

        
if __name__ == '__main__':
    orc = Orc('Banana')
    farting_orc = FartingDecorator(Orc('Mogka'))
    farting_tauren = FartingDecorator(Tauren('Muuu'))
    
    orc.attack()
    farting_orc.attack()
    farting_tauren.attack()
    
