"""
composite = contains group of objects of the same type
"""


class Orc:

    def __init__(self, name):
        self.name = name
        self.killed_orcs = []
    
    def add_killed_orc(self, orc):
        self.killed_orcs.append(orc)
    
    @staticmethod
    def show_killed_orcs(orc, indent=''):
        print('%s%s, killed orcs: %s' % 
              (indent, orc.name, len(orc.killed_orcs)))
        for killed_orc in orc.killed_orcs:
            Orc.show_killed_orcs(killed_orc, '%s    ' % indent) 


if __name__ == '__main__':
    mogka = Orc('Mogka')
    ra = Orc('Ra')
    banana = Orc('Banana')
    igra = Orc('Igra')
    
    igra.add_killed_orc(banana)
    mogka.add_killed_orc(igra)
    mogka.add_killed_orc(ra)
    Orc.show_killed_orcs(mogka)
