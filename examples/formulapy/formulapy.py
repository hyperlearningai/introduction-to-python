#!/usr/bin/env python3
"""Car racing game written in Python.

"""

import time


class Car:

    number_wheels = 4

    def __init__(self, number_doors, registration_number, make,
                 model, year_manufactured, maximum_speed,
                 acceleration_rate, deceleration_rate):
        self.number_doors = number_doors
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year_manufactured = year_manufactured
        self.maximum_speed = maximum_speed
        self.acceleration_rate = acceleration_rate
        self.deceleration_rate = deceleration_rate
        self.mileage_miles = 0
        self.speed_mph = 0

    def __str__(self):
        return type(self).__name__ + str(vars(self))

    def accelerate(self):
        while self.speed_mph < self.maximum_speed:
            time.sleep(1)
            self.speed_mph += self.acceleration_rate

    def brake(self):
        while self.speed_mph > 0:
            time.sleep(1)
            self.speed_mph -= self.deceleration_rate

    def turn_left(self):
        pass

    def turn_right(self):
        pass
