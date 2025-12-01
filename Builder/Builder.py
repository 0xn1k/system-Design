from abc import ABC, abstractmethod
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.door = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.door} door"

class HouseBuilder(ABC):

    @abstractmethod
    def build_walls(self): pass

    @abstractmethod
    def build_roof(self): pass

    @abstractmethod
    def build_door(self): pass

    @abstractmethod
    def get_house(self): pass

class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "wooden"

    def build_roof(self):
        self.house.roof = "wooden"

    def build_door(self):
        self.house.door = "brown wooden"

    def get_house(self):
        return self.house


class GlassHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "glass"

    def build_roof(self):
        self.house.roof = "transparent glass"

    def build_door(self):
        self.house.door = "sliding glass"

    def get_house(self):
        return self.house

class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_door()
        return self.builder.get_house()
        
director = Director(WoodenHouseBuilder())
wooden_house = director.construct_house()
print(wooden_house)

director = Director(GlassHouseBuilder())
glass_house = director.construct_house()
print(glass_house)
