class Pet:
    def __init__(self, brain: bool, name: str, price: int):
        super().__init__(Goldfish, name=name, price=price, type='fish')
        self.type = type
        print("Created a Goldfish")

    def get_price_tax(self):
        return self.price * .1

class Goldfish(Pet):
    def __init__(self, brain: bool, name: str, price: int):




