"""
If you have several ways to do the same thing
can use Strategy pattern, where each different algorithm is
in separate class.
Context object has Strategy and based on that strategy
the action is performed in different ways.
"""
import abc


class Strategy:
    
    @abc.abstractmethod
    def attack(self):
        pass


class ArchersStrategy(Strategy):
    
    def attack(self):
        print('attacking with archers')

        
class CavalryStrategy(Strategy):
    
    def attack(self):
        print('attacking with cavalry')


class InfantryStrategy(Strategy):
    
    def attack(self):
        print('attacking with infantry')


class ArmyContext:
    
    def __init__(self):
        self.strategy = None
    
    def attack_with_strategy(self):
        if self.strategy:
            self.strategy.attack()
        else:
            print('Need strategy to attack')


def run():
    army = ArmyContext()
    archers_strategy = ArchersStrategy()
    cavalry_strategy = CavalryStrategy()
    infantry_strategy = InfantryStrategy()
    
    army.attack_with_strategy()
    army.strategy = archers_strategy
    army.attack_with_strategy()
    army.strategy = cavalry_strategy
    army.attack_with_strategy()
    army.strategy = infantry_strategy
    army.attack_with_strategy()


if __name__ == '__main__':
    run()
