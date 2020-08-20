#!/usr/bin/env python3
"""Collection of useful tools for working with numbers.

This module demonstrates the creation and usage of modules in Python.
The documentation standard for modules is to provide a docstring at the top
of the module script file. This docstring consists of a one-line summary
followed by a more detailed description of the module. Sections may also be
included in module docstrings, and are created with a section header and a 
colon followed by a block of indented text. Refer to
https://www.python.org/dev/peps/pep-0008/ for the PEP 8 style guide for
Python code for further information.

Attributes:
    mobius_phi (float): Module level variables are documented in
    either the ``Attributes`` section of the module docstring, or in an
    inline docstring immediately following the variable. Either form is
    acceptable, however HyperLearning AI prefer module level variables be
    documented in the module docstring. In this case, mobius_phi is a
    constant value used as part of the Mobius test to determine whether
    a given number is a Fibonacci number or not.
 
"""

import math

mobius_phi = 0.5 + 0.5 * math.sqrt(5.0)


def is_int(num):
    """Test whether a given number is an integer or not.

    Tests whether a given number is an integer or not using the in-built
    isinstance() Python function, which returns True if the given object
    is of the specified type, otherwise False.

    Args:
        num (int): The number to test whether it is an integer

    Returns:
        bool: True if num is an integer, otherwise False.

    """

    return isinstance(num, int)


def is_even(num):
    """Test whether a given number is even or not.

    Tests whether a given number is even or not using the modulo operator.

    Args:
        num (int): The number to test whether it is even

    Returns:
        bool: True if num is even, otherwise False

    """

    return True if num % 2 == 0 else False


def is_prime(num):
    """Test whether a given number is a prime number or not.

    Tests whether a given number is a prime number or not, by first testing
    whether it is 0, 1, negative or not a whole number. If neither of these
    conditions are met, then the function proceeds to test whether the given
    number can be divided by the numbers from 2 to the floor division of the
    given number by 2 without a remainder. If not, then the given number is
    indeed a prime number.

    Args:
        num (int): The number to test whether it is a prime number

    Returns:
        bool: True if num is a prime number, otherwise False

    """

    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def is_fibonacci(num):
    """Test whether a given number is a Fibonacci number or not.

    Tests whether a given number is a Fibonacci number or not using
    the Mobius Test.

    Args:
        num (int): The number to test whether it is a Fibonacci number

    Returns:
        bool: True if num is a Fibonacci number, otherwise False

    """

    a = mobius_phi * num
    return num == 0 or abs(round(a) - a) < 1.0 / num


def is_perfect_square(num):
    """Test whether a given number is a perfect square.

    Tests whether a given number is a perfect square or not based
    on the Babylonian method for computing square roots.

    Args:
        num (int): The number to test whether it is a perfect square

    Returns:
        bool: True if num is a perfect square, otherwise False

    """

    if num < 0:
        return False
    if num == 0 or num == 1:
        return True

    x = num // 2
    y = {x}
    while x * x != num:
        x = (x + (num // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True
