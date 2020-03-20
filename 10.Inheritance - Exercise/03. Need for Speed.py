class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        liters = kilometers * self.fuel_consumption
        if not self.fuel < liters:
            self.fuel -= liters


class Motorcycle(Vehicle):
    pass


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8


class CrossMotorcycle(Motorcycle):
    pass


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3


class FamilyCar(Car):
    pass


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10



m = Motorcycle(15, 2000)
m.drive(100)
print(m.__dict__)
r = RaceMotorcycle(15, 2000)
r.drive(100)
r.drive(50)
r.drive(50)
print(r.__dict__)
m.drive(100)
print(m.__dict__)

