class ModelPerson:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
class ViewPerson:
    
    def display(self, name, age):
        print('name: %s, age: %s' % (name, age))


class ControllerPerson:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view        
    
    def set_person_name(self, name):
        self.model.name = name
    
    def set_person_age(self, age):
        self.model.age = age
    
    def update_view(self):
        self.view.display(self.model.name, self.model.age)


def run():
    model = ModelPerson('Marko', 26)
    view = ViewPerson()
    controller = ControllerPerson(model, view)
    controller.update_view()
    controller.set_person_name('Ivan')
    controller.set_person_age(30)
    controller.update_view()

    
if __name__ == '__main__':
    run()
    
