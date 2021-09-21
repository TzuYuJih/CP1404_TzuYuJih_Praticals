from prac_08.car import Car
import random

class Unreliable_car(Car):
    def __init__(self, name, fuel, reliablility):
        self.name = name
        self.fuel = fuel
        self.reliablility = reliablility
    def drive(self, distance):
        if random.randint(0, 100) < self.reliablility:
            if distance >= self.fuel:
                self.fuel = 0
            else:
                self.fuel -= distance
        return distance

