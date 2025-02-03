"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_06.base import Vehicle
from homework_06.engine import Engine


class Car(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self._engine = None

    def set_engine(self, engine: Engine):
        self._engine = engine
