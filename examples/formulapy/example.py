#!/usr/bin/env python3
"""Example Car Class.

This module demonstrates how to define (and document) a class in Python, in
this case one where instances of the class are car objects. This class
demonstrates how to use the __init__() and __str__() methods respectively,
as well as how to define custom class methods including usage of the self
parameter. Finally, it demonstrates the difference between class and instance
variables.

"""

import time
from datetime import datetime


class Car:
    """Example car class.

    This class is used to demonstrate how to define (and document) classes
    in Python. This class demonstrates the __init__(), __str__() and custom
    methods, as well as the self parameter, and the difference between class
    and instance variables. Class docstrings, by convention, start with a
    one line summary followed by a more detailed description. The docstring
    goes on to describe class attributes. Class methods are documented with
    their own docstring i.e. function docstrings.

    Attributes:
        number_doors (int): The number of doors.
        registration_number (str): The unique car registration number.
        make (str): The car make, for example McLaren.
        model (str): The car model, for example P1.
        year_manufactured (int): The year of manufacture.
        maximum_speed (int): The maximum speed of the car, in miles per hour.
        acceleration_rate (int): The constant acceleration rate in miles/second.
        deceleration_rate (int): The constant deceleration rate in miles/second.

    """

    number_wheels = 4

    def __init__(self, number_doors, registration_number, make,
                 model, year_manufactured, maximum_speed,
                 acceleration_rate, deceleration_rate):
        """Example of a docstring on the __init__() method.

        The __init__() method, just like any other function in Python, should
        be documented with a docstring, starting with a one line summary
        followed by a more detailed description. Following the detailed
        description should follow a description of each of the arguments,
        but not including the self parameter.

        Args:
            number_doors (int): The number of doors.
            registration_number (str): The unique car registration number.
            make (str): The car make, for example McLaren.
            model (str): The car model, for example P1.
            year_manufactured (int): The year of manufacture.
            maximum_speed (int): The maximum speed of the car in miles per hour.
            acceleration_rate (int): Constant acceleration rate in miles/second.
            deceleration_rate (int): Constant deceleration rate in miles/second.
        """

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
        """Override the __str__() method to return the class name followed
        by the string representation of the object's namespace dictionary.
        """
        return type(self).__name__ + str(vars(self))

    def accelerate(self):
        """A method to model car acceleration.

        This method models the acceleration of a car. For the purposes of this
        course, the modelling of acceleration is trivial where the speed of the
        car increases by a constant rate every second until the maximum speed
        of the car is reached.

        Returns:
            None
        """

        self.log_speed()
        while self.speed_mph < self.maximum_speed:
            time.sleep(1)
            if (self.speed_mph + self.acceleration_rate) > self.maximum_speed:
                self.speed_mph = self.maximum_speed
                self.log_speed()
                break
            else:
                self.speed_mph += self.acceleration_rate
            self.log_speed()

    def brake(self):
        """A method to model a car braking.

        This method models a car braking. For the purposes of this course,
        the modelling of braking is trivial where the speed of the car
        decreases by a constant rate every second until the speed of the car is
        zero.

        Returns:
            None
        """

        self.log_speed()
        while self.speed_mph > 0:
            time.sleep(1)
            if (self.speed_mph - self.deceleration_rate) < 0:
                self.speed_mph = 0
                self.log_speed()
                break
            else:
                self.speed_mph -= self.deceleration_rate
            self.log_speed()

    def turn_left(self):
        """A method to model a car turning left.

        This method models a car turning left. For the time being, and in this
        module, this method is just a placeholder and does nothing.

        Returns:
            None

        """
        pass

    def turn_right(self):
        """A method to model a car turning right.

        This method models a car turning right. For the time being, and in this
        module, this method is just a placeholder and does nothing.

        Returns:
            None

        """
        pass

    def log_speed(self):
        """A method to log the current speed of the car.

        This method logs the current speed of the car. For the purposes of this
        course, the logging of speed is trivial and is implemented by the
        print() function displaying a message to standard out.

        Returns:
             None

        """

        print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: '
              f'{self.make} {self.model} current speed: '
              f'{self.speed_mph}mph')
