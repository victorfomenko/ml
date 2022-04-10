import exceptions
from vehicle import Vehicle


class Plane(Vehicle):
    cargo = 10
    max_cargo = int

    def __init__(self, weight=None, fuel=None, fuel_consumption=None, max_cargo=100):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        cargo_total = self.cargo + value
        if cargo_total <= self.max_cargo:
            self.cargo = cargo_total
        else:
            raise exceptions.CargoOverload()

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before
