from abc import ABC

from homework_06.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=60, fuel_consumption=5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print('Транспортное средство запущено')
            else:
                raise LowFuelError
        else:
            print('Транспортное средство уже в запущенном состоянии')

    def move(self, distance):
        result = self.fuel_consumption * distance
        if not self.started:
            raise ValueError('Транспортное средство не запущено')
        elif self.fuel - result < 0:
            raise NotEnoughFuel
        self.fuel -= result
        print(f'Остаток топлива: {self.fuel}')
