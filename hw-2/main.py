from vehicle import Vehicle
from plane import Plane

# Vehicle
vehicle = Vehicle(False)
vehicle.fuel = 100
vehicle.fuel_consumption = 10
vehicle.move(1)
vehicle.start()

# Plane
plane = Plane(100)
plane.load_cargo(90)
