"""
Not really useful, just want to have example for 
this design pattern
"""


class Orc:

    def __init__(self, name, kills):
        self.name = name
        self.kills = kills


class Filter:

    def filter(self, orcs_list):
        raise NotImplementedError()


class EliteKillersFilter(Filter):

    def filter(self, orcs):
        return [orc for orc in orcs if orc.kills > 100]
    
    
class OrcsWithoutKillFilter(Filter):

    def filter(self, orcs):
        return [orc for orc in orcs if orc.kills == 0]


def print_orcs(orcs, msg):
    print(msg)
    for orc in orcs:
        print('%s, kills: %s' % (orc.name, orc.kills))


if __name__ == '__main__':
    orcs = [
        Orc('Mogka', 212),
        Orc('Ra', 199),
        Orc('Mofo', 12),
        Orc('Banana', 0)
    ]
    r = EliteKillersFilter().filter(orcs)
    print_orcs(r, 'Elite Killers')
    r = OrcsWithoutKillFilter().filter(orcs)
    print_orcs(r, '0-Kill orcs')
