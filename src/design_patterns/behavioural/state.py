"""
Object (context) changes its behaviour based
on its state

Can be used for long if/switch structures where each
case contains some logic
"""


class ContextLightSwitch:
    
    def __init__(self):
        self.state = None
        self.change_state(StateBulbOff())
        
    def change_state(self, state):
        self.state = state
        self.state.context = self
    
    def switch_on(self): 
        self.state.switch_on()
    
    def switch_off(self):
        self.state.switch_off()


class State:
    
    def __init__(self):
        self.context = None
    
    def switch_on(self):
        raise NotImplementedError()
    
    def switch_off(self):
        raise NotImplementedError()    


class StateBulbOff(State):
    
    def switch_on(self):
        print('bulb ON')
        self.context.change_state(StateBulbOn())
    
    def switch_off(self):
        print('bulb already OFF')


class StateBulbOn(State):
    
    def switch_on(self):
        print('bulb already ON')
    
    def switch_off(self):
        print('bulb OFF')
        self.context.change_state(StateBulbOff())


def run():
    light_switch = ContextLightSwitch()
    light_switch.switch_on()
    light_switch.switch_on()
    light_switch.switch_off()
    light_switch.switch_off()
    

if __name__ == '__main__':
    run()
