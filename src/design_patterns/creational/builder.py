

class Meal:

    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def show_items(self):
        for item in self.items:
            print('%s - %.2f' % (item.get_name(), item.get_price()))
    
    def get_price(self):
        price = 0
        for item in self.items:
            price += item.get_price()
        
        return round(price, 2)

    
class Package:
    
    def get_price(self):
        return 0.05

    
class BurgerPackage(Package):
    
    def get_price(self):
        return super().get_price() + 0.05

    
class BottlePackage(Package):
    
    def get_price(self):
        return super().get_price() + 0.25


class Item:

    def get_price(self):
        return self.package_price() + self.item_price()
    
    def get_name(self):
        raise NotImplementedError()

        
class UnspecifiedBurger(Item):
    
    def __init__(self):
        self.package = BurgerPackage()
    
    def package_price(self):
        return self.package.get_price()

    
class CheeseBurger(UnspecifiedBurger):
    
    def item_price(self):
        return 1.2
    
    def get_name(self):
        return 'cheese burger'

    
class BananaBurger(UnspecifiedBurger):
    
    def item_price(self):
        return 1.55
    
    def get_name(self):
        return 'banana burger'


class UnspecifiedBottleDrink(Item):
    
    def __init__(self):
        self.package = BottlePackage()
    
    def package_price(self):
        return self.package.get_price()


class Fanta(UnspecifiedBottleDrink):
    
    def item_price(self):
        return 0.75
    
    def get_name(self):
        return 'fanta'

    
class Airan(UnspecifiedBottleDrink):
    
    def item_price(self):
        return 0.45
    
    def get_name(self):
        return 'airan'


if __name__ == '__main__':
    meal = Meal()
    meal.add_item(CheeseBurger())
    meal.add_item(CheeseBurger())
    meal.add_item(BananaBurger())
    meal.add_item(Airan())
    meal.add_item(Fanta())
    meal.show_items()
    print('-------------\nTotal %.2f' % meal.get_price())

