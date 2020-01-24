class HouseBuilder:
    
    def __init__(self):
        self.parts = []
    
    def build_floor(self):
        # depends on the use case which is more appropriate:
        # fail or skip if not implemented
        # raise NotImplementedError() 
        return self
    
    def build_walls(self):
        return self
    
    def build_windows(self):
        return self
    
    def build_roof(self):
        return self
    
    def build_swimming_pool(self):
        return self
    
    def build_garden(self):
        return self
    
    def build_porch(self):
        return self
    
    def reset(self):
        self.parts = []
        
    def show_parts(self):
        print(self.parts)

    
class WoodenHouseBuilder(HouseBuilder):
    
    def build_floor(self):
        print('build wooden floor')
        self.parts.append('wooden floor')
        return self
    
    def build_walls(self):
        print('build wooden walls')
        self.parts.append('wooden walls')
        return self
    
    def build_windows(self):
        print('build windows with wooden frames')
        self.parts.append('wooden windows')
        return self
    
    def build_roof(self):
        print('build wooden roof')
        self.parts.append('wooden roof')
        return self
        
        
class StoneHouseBuilder(HouseBuilder):
    
    def build_floor(self):
        print('build stone floor')
        self.parts.append('stone roof')
        return self
    
    def build_walls(self):
        print('build stone walls')
        self.parts.append('stone walls')
        return self
    
    def build_windows(self):
        print('build windows with stone frames')
        self.parts.append('stone windows')
        return self
    
    def build_roof(self):
        print('build stone roof')
        self.parts.append('stone roof')
        return self
    
    def build_swimming_pool(self):
        print('build stone swimming pool')
        self.parts.append('stone pool')
        return self
    
    def build_garden(self):
        print('build garden with stone fence')
        self.parts.append('stone garden')
        return self
    
    def build_porch(self):
        print('build stone porch')
        self.parts.append('stone porch')
        return self

    
# optional, for commonly used steps in given order
class Director:
    
    def __init__(self, builder=None):
        self.builder = builder
        
    def build_cheap_house(self):
        (self.builder.build_floor()
         .build_walls()
         .build_windows()
         .build_roof())
        
    def build_expensive_house(self):
        self.build_cheap_house()
        (self.builder.build_porch()
         .build_swimming_pool()
         .build_garden())

    
def run():
    wooden_house_builder = WoodenHouseBuilder()
    stone_house_builder = StoneHouseBuilder()
    builders = [wooden_house_builder, stone_house_builder]
    director = Director()
    for builder in builders:
        director.builder = builder
        director.build_cheap_house()
        builder.show_parts()
        builder.reset()
        director.build_expensive_house()
        builder.show_parts()


if __name__ == '__main__':
    run()
