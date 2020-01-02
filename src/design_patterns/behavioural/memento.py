"""
Object can save its states and restore to previous state
"""
from datetime import datetime
import json


class Memento:
    """
    State holder
    """

    def __init__(self, state):
        self.state = state
        self.ts = datetime.utcnow()
    
    def __str__(self):
        return 'ts: %s, state: %s' % (self.ts, str(self.state))
        

class Originator:
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def get_state(self):
        data = {
            'name': self.name,
            'hp': self.hp
        }
        return json.dumps(data)
    
    def set_state(self, state):

        def fail():
            raise Exception('Invalid state: %s' % str(state))
            
        if isinstance(state, str):
            state = json.loads(state)
            
        if not isinstance(state, dict):
            fail()

        try:
            self.name = state['name']
            self.hp = state['hp']
        except Exception as ex:
            print(ex)
            fail()
        
    def __str__(self):
        return 'name: %s, hp: %s' % (self.name, self.hp)


class Caretaker:

    def __init__(self, originator):
        self.originator = originator
        self.mementos = []
        
    def save(self):
        self.mementos.append(
            Memento(self.originator.get_state())
        )
    
    def restore(self):
        if not self.mementos:
            return False
        
        memento = self.mementos.pop()
        self.originator.set_state(memento.state)
        return True
        
    def show_states(self):
        for memento in self.mementos:
            print(memento)


def run():
    originator = Originator('Mojo', hp=100)
    care_taker = Caretaker(originator)    
    
    care_taker.save()
    originator.hp = 90
    care_taker.save()
    originator.hp = 50
    care_taker.save()
    originator.hp = 10
    
    care_taker.show_states()
    while True:
        print('originator: %s' % originator)
        if not care_taker.restore():
            break


if __name__ == '__main__':
    run()
