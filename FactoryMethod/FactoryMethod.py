# factory element
class Cappucino:
    def prepare(self):
        print("prepare cappucino")


class Latte:
    def prepare(self):
        print("prepate latte")

class Espresso:
    def prepare(self):
        print("prepare espresso")


# let factory decide which  factory element to call
class FactoryClass:
    def create_coffee(self, coffee_type):
        if coffee_type == "cappucino":
            return Cappucino()
        elif coffee_type == "latte":
            return Latte()
        elif coffee_type == "espresso":
            return Espresso()
        else:
            raise ValueError("unknow coffe type")

# create factory class and consume it 
factory= FactoryClass();
latte = factory.create_coffee("latte")
latte.prepare()