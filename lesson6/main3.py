class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position("Ivan", "Pupkin", "Senior Developer", 100000, 50000)
worker2 = Position("Stepan", "Razin", "Manager ", 200000, 100000)
print(f"Full name: {worker1.get_full_name()}, Total Income: {worker1.get_total_income()}")
print(f"Full name: {worker2.get_full_name()}, Total Income: {worker2.get_total_income()}")

