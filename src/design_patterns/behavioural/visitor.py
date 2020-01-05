

class DataExtractVisitor:
    
    def __init__(self):
        self.data = []
    
    def extract_data_from_human(self, human):
        raise NotImplementedError()
    
    def extract_data_from_alien(self, alien):
        raise NotImplementedError()

        
class NameExtractVisitor(DataExtractVisitor):
    
    def extract_data_from_human(self, human):
        self.data.append('human name: %s' % human.name)

    def extract_data_from_alien(self, alien):
        self.data.append('alien name: %s' % alien.name)

    
class AgeExtractVisitor(DataExtractVisitor):
    
    def extract_data_from_human(self, human):
        self.data.append('human age: %s' % human.age)

    def extract_data_from_alien(self, alien):
        self.data.append('alien age: %s' % alien.age)


class Humanoid:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Human(Humanoid):
    
    def accept_data_extract_visitor(self, visitor):
        visitor.extract_data_from_human(self)
        

class Alien(Humanoid):
    
    def accept_data_extract_visitor(self, visitor):
        visitor.extract_data_from_alien(self)


def run():
    alien = Alien('AU', 384)
    human = Human('Bah', 20)
    name_extractor = NameExtractVisitor()
    age_extractor = AgeExtractVisitor()
    alien.accept_data_extract_visitor(name_extractor)
    human.accept_data_extract_visitor(name_extractor)
    alien.accept_data_extract_visitor(age_extractor)
    human.accept_data_extract_visitor(age_extractor)
    print(name_extractor.data)
    print(age_extractor.data)

    
if __name__ == '__main__':
    run()
