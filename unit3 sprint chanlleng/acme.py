import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif 0.5 <= ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle."
        elif 10 <= product < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
