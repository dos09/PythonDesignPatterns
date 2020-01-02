"""
Observers subscribe to listen for event on Subject.
When the event on Subject is triggered all subscribed
Observers are notified.
"""


class Subject:
    
    def __init__(self):
        self._observers = {}
        
    def add_observer(self, observer):
        self._observers[id(observer)] = observer
        
    def remove_observer(self, observer):
        observer_id = id(observer)
        if observer_id in self._observers:
            del self._observers[observer_id]

    def notify(self):
        for observer in self._observers.values():
            observer.update(self)


class Warrior(Subject):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def die(self):
        print('%s died' % self.name)
        self.notify()

        
class Observer:
    
    def update(self, subject):
        print('observer dummy update')
        pass


class Valkyrie(Observer):
    
    def update(self, subject):
        self.resurrect(subject)
        
    def resurrect(self, warrior):
        print('valkyrie resurrected %s' % warrior.name)

        
class Shaman(Observer):
    
    def update(self, subject):
        self.heal(subject)
        
    def heal(self, warrior):
        print('shaman healed %s' % warrior.name)


if __name__ == '__main__':
    warrior = Warrior('Ra')
    valkyrie = Valkyrie()
    shaman = Shaman()
    warrior.add_observer(valkyrie)
    warrior.add_observer(shaman)
    warrior.die()
    warrior.remove_observer(shaman)
    warrior.die()
