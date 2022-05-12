class Store:
    def __init__(self):
        self._stock = []
        self.total_cost = 0

    def __str__(self):
        return '\n'.join([f"{i + 1}. {it[1]} items of {it[0]} " for i, it in enumerate(self._stock)]) + \
               f"\nin stock\nTotal cost: {self.total_cost}"

    def receive_items(self, item, num):
        if isinstance(item, Technics) and isinstance(num, int):
            if any(item in x for x in self._stock):
                for it in self._stock:
                    if item is it[0]:
                        it[1] = it[1] + num
                        break
            else:
                self._stock.append([item, num])
            self.total_cost = self.sum_total()
        else:
            print("some arguments not meeting criteria")

    def transfer(self, item, num):
        if isinstance(item, Technics) and isinstance(num, int):
            if any(item in x for x in self._stock):
                for it in self._stock:
                    if item is it[0]:
                        it[1] = it[1] - num
                        if it[1] <= 0:
                            self._stock.remove(it)
                        break
            self.total_cost = self.sum_total()
        else:
            print("some arguments not meeting criteria")

    def sum_total(self):
        running_sum = 0
        for it in self._stock:
            running_sum = running_sum + it[0].price * it[1]
        return running_sum


class Technics:
    def __init__(self, brand, name, price):
        self.brand = self.validate_inputs(brand, str, "Brand")
        self.name = self.validate_inputs(name, str, "Name")
        self.price = self.validate_inputs(price, (float, int), "Price")

    @staticmethod
    def validate_inputs(val, val_type, prop):
        if isinstance(val, val_type):
            return val
        else:
            print(f"{prop} value is not meeting conditions for {val_type}")
            return None

    def __str__(self):
        return f"Printer {self.brand} {self.name}. Price is {self.price}"


class Printer(Technics):
    def __init__(self, brand, name, price, color):
        super().__init__(brand, name, price)
        self.type = self.validate_inputs(color, str, "Type")

    def __repr__(self):
        return f"Printer {self.brand} {self.name}. Type is {self.type}. Price is {self.price}"


class Scanner(Technics):
    def __init__(self, brand, name, price, maxsize):
        super().__init__(brand, name, price)
        self.maxsize = self.validate_inputs(maxsize, str, "Maximum size of paper")

    def __repr__(self):
        return f"Scanner {self.brand} {self.name}. Size is {self.maxsize}. Price is {self.price}"


class Copier(Technics):
    def __init__(self, brand, name, price, maxsize, speed):
        super().__init__(brand, name, price)
        self.maxsize = self.validate_inputs(maxsize, str, "Maximum size of paper")
        self.speed = self.validate_inputs(speed, int, "Copying speed")

    def __repr__(self):
        return f"Printer {self.brand} {self.name}. Speed is {self.speed}. Price is {self.price}"


if __name__ == "__main__":
    store1 = Store()
    item1 = Printer("Epson", "L-805", 10000, "color")
    item2 = Scanner("Dell", "S-500", 1000, "A4")
    item3 = Copier("HP", "H-600", 40000, "A3", 500)
    item4 = Printer(3, "HP", 300, "color")
    store1.receive_items(item1, 3)
    store1.receive_items(item1, 2)
    store1.receive_items(item2, 5)
    store1.receive_items(item3, 10)
    store1.receive_items(item4, 10)
    print(store1)
    store1.transfer(item3, 10)
    print(store1)
