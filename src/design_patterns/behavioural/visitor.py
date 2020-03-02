"""
Visitor is a behavioral design pattern that lets you separate algorithms 
from the objects on which they operate.

If you have different classes and must add some functionality to them,
but don't want to change these classes (avoid breaking something)
can create Visitor class where to store the methods. Each class will have
method accepting visitor and calling the appropriate visitor's method.
Example:
    -having 
    
    class XMLData
    class CSVData
    
    - need to add functionality to extract data to JSON
    - create
    
    class Visitor:
        def xml_to_json(obj)...
        def csv_to_json(obj)...
        
    - change
    
    class XMLData
        def accept(self, visitor):
            visitor.xml_to_json(self)
            
    class CSVData
        def accept(self, visitor):
            visitor.csv_to_json(self)
"""


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
