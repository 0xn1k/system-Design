
from abc import ABC , abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Table(ABC):
    @abstractmethod
    def eat(self):
        pass

class FurnitureFactory:
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

class ModernChair(Chair):
    def sit(self):
        print("sitting on modern chair")

class VictorianChair(Chair):
    def sit(self):
        print("sitting on victorain chair")

class ModernTable(Table):
    def eat(self):
        print("eating on modern chair")

class VictorinTable(Table):
    def eat(self):
        print("eating on victorian chair")


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair();
    def create_table(self):
        return ModernTable();

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair();
    def create_table(self):
        return VictorinTable();


def setup_room(factory : FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    chair.sit()
    table.eat()


setup_room(ModernFurnitureFactory())
setup_room(VictorianFurnitureFactory())