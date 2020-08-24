#!/usr/bin/env python3
"""Data model describing the domain of modern vehicles.

This module contains a series of class definitions representing our chosen
data model to describe the domain of modern vehicles. The module contains a
Vehicle superclass definition designed to model general vehicles. Thereafter
the module contains a RoadVehicle subclass definition which inherits attributes
and methods common to all vehicles from the Vehicle superclass, in addition to
attributes and methods specific to road vehicles. Finally the module contains a
Car subclass definition which inherits attributes and methods common to all
road vehicles from the RoadVehicle superclass, in addition to attributes and
methods specific to cars.

"""

import time
from datetime import date, datetime


class Vehicle:

    def __init__(self, number_engines, engine_horsepower_kw,
                 chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                 make, model, year_manufactured, maximum_speed_mph,
                 acceleration_rate_mps, deceleration_rate_mps):
        """Initialise instances of the Vehicle class."""

        self.number_engines = number_engines
        self.engine_horsepower_kw = engine_horsepower_kw
        self.chassis_height_mm = chassis_height_mm
        self.chassis_width_mm = chassis_width_mm
        self.chassis_depth_mm = chassis_depth_mm
        self.make = make
        self.model = model
        self.year_manufactured = year_manufactured
        self.maximum_speed_mph = maximum_speed_mph
        self.acceleration_rate_mps = acceleration_rate_mps
        self.deceleration_rate_mps = deceleration_rate_mps
        self.mileage_miles = 0
        self.speed_mph = 0

    def __str__(self):
        """Override the __str__() method to return the class name followed
        by the string representation of the object's namespace dictionary.
        """
        return type(self).__name__ + str(vars(self))

    def accelerate(self):
        """A method to model vehicle acceleration.

        This method models the acceleration of a vehicle. For the purposes of
        this course, the modelling of acceleration is trivial where the speed
        of the vehicle increases by a constant rate every second until the
        maximum speed of the vehicle is reached.

        Returns:
            None
        """

        self.log_speed()
        while self.speed_mph < self.maximum_speed_mph:
            time.sleep(1)
            if (self.speed_mph + self.acceleration_rate_mps) \
                    > self.maximum_speed_mph:
                self.speed_mph = self.maximum_speed_mph
                self.log_speed()
                break
            else:
                self.speed_mph += self.acceleration_rate_mps
            self.log_speed()

    def brake(self):
        """A method to model a vehicle braking.

        This method models a vehicle braking. For the purposes of this course,
        the modelling of braking is trivial where the speed of the vehicle
        decreases by a constant rate every second until the speed of the
        vehicle is zero.

        Returns:
            None
        """

        self.log_speed()
        while self.speed_mph > 0:
            time.sleep(1)
            if (self.speed_mph - self.deceleration_rate_mps) < 0:
                self.speed_mph = 0
                self.log_speed()
                break
            else:
                self.speed_mph -= self.deceleration_rate_mps
            self.log_speed()

    def turn_left(self):
        """A method to model a vehicle turning left."""
        pass

    def turn_right(self):
        """A method to model a vehicle turning right."""
        pass

    def log_speed(self):
        """A method to log the current speed of a vehicle.

        This method logs the current speed of a vehicle. For the purposes of
        this course, the logging of speed is trivial and is implemented by the
        print() function displaying a message to standard out.

        Returns:
             None

        """

        print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: '
              f'{self.make} {self.model} current speed: '
              f'{self.speed_mph}mph')


class RoadVehicle(Vehicle):

    def __init__(self, number_engines, engine_horsepower_kw,
                 chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                 make, model, year_manufactured, maximum_speed_mph,
                 acceleration_rate_mps, deceleration_rate_mps,
                 number_wheels, registration_number):
        """Initialise instances of the RoadVehicle class."""

        super().__init__(number_engines, engine_horsepower_kw,
                         chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                         make, model, year_manufactured, maximum_speed_mph,
                         acceleration_rate_mps, deceleration_rate_mps)
        self.number_wheels = number_wheels
        self.registration_number = registration_number
        self.last_mot_date = date.today().strftime("%d/%m/%Y")

    def signal(self):
        """A method to model a road vehicle signalling."""
        pass

    def reverse(self):
        """A method to model a road vehicle reversing."""
        pass


class Car(RoadVehicle):

    number_wheels = 4

    def __init__(self, number_engines, engine_horsepower_kw,
                 chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                 make, model, year_manufactured, maximum_speed_mph,
                 acceleration_rate_mps, deceleration_rate_mps,
                 registration_number):
        """Initialise instances of the Car class."""

        super().__init__(number_engines, engine_horsepower_kw,
                         chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                         make, model, year_manufactured, maximum_speed_mph,
                         acceleration_rate_mps, deceleration_rate_mps,
                         self.number_wheels, registration_number)

    def handbrake_turn(self):
        """A method to model a car making a handbrake turn."""
        pass

    def avoid_collision(self):
        """A method to model a car avoiding an oncoming collision."""
        super().turn_left()
        super().brake()


class Aircraft(Vehicle):

    def __init__(self, number_engines, engine_horsepower_kw,
                 chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                 make, model, year_manufactured, maximum_speed_mph,
                 acceleration_rate_mps, deceleration_rate_mps,
                 minimum_speed_mph):
        """Initialise instances of the Aircraft class."""

        super().__init__(number_engines, engine_horsepower_kw,
                         chassis_height_mm, chassis_width_mm, chassis_depth_mm,
                         make, model, year_manufactured, maximum_speed_mph,
                         acceleration_rate_mps, deceleration_rate_mps)
        self.minimum_speed_mph = minimum_speed_mph

    def brake(self):
        """A method to model an aircraft braking.

        This method overrides the brake() method in the Vehicle class and
        instead provides a trivial model of an aircraft braking where the
        speed of the aircraft decreases by a constant rate every second until
        the speed of the aircraft reaches its minimum speed to maintain flight.

        Returns:
            None
        """

        self.log_speed()
        while self.speed_mph >= self.minimum_speed_mph:
            time.sleep(1)
            if (self.speed_mph - self.deceleration_rate_mps) \
                    < self.minimum_speed_mph:
                self.speed_mph = self.minimum_speed_mph
                self.log_speed()
                break
            else:
                self.speed_mph -= self.deceleration_rate_mps
            self.log_speed()
