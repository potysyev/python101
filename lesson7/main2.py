class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


coat1 = Coat("gucci", 1)
suit = Suit("Armani", 1)
print(f"Fabric consumption for coat {coat1.fabric_consumption} and suit {suit.fabric_consumption}")
