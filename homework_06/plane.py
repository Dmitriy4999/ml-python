"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_06.base import Vehicle
from homework_06.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, max_cargo, **kwargs):
        super().__init__(kwargs)
        self._max_cargo = max_cargo
        self._cargo = None

    def set_cargo(self, cargo):
        if self._max_cargo - cargo > 0:
            self._cargo = cargo
            print(f'Доступно для погрузки: {self._max_cargo - self._cargo}')
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        self._cargo = None
        print('Груз выгружен')
