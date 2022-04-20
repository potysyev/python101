class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} has started")

    def stop(self):
        print(f"Car {self.name} has stopped")

    def turn(self, direction):
        print(f"Car {self.name} turned {direction}")

    def show_speed(self):
        print(f"Car {self.name} is going with speed {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Car is speeding")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Car is speeding")


class PoliceCar(Car):
    pass


car1 = TownCar('BMW', 'black', 70)
car2 = SportCar('Lamboghini', 'red', 110)
car3 = WorkCar('VAZ', 'white', 50)
car4 = PoliceCar('Volga', 'blue', 100, is_police=True)
car1.show_speed()
car3.show_speed()

car4.go()
car4.turn("right")
car4.stop()
print(car4.is_police)
