from homework_06.car import Car
from homework_06.engine import Engine
from homework_06.plane import Plane

car = Car()
car.set_engine(Engine(10, 20))
car.start()
car.start()
car.move(5)

plane = Plane(100)
plane.set_cargo(90)
plane.remove_all_cargo()
plane.set_cargo(90)
