#!/usr/bin/env python3
"""Collection of useful tools for working with tuple objects.

This module demonstrates the creation and usage of modules in Python.
The documentation standard for modules is to provide a docstring at the top
of the module script file. This docstring consists of a one-line summary
followed by a more detailed description of the module. Sections may also be
included in module docstrings, and are created with a section header and a
colon followed by a block of indented text. Refer to
https://www.python.org/dev/peps/pep-0008/ for the PEP 8 style guide for
Python code for further information.

"""


def convert_to_dict(my_tuple):
    """Convert a given tuple of (value, key) tuples to a dictionary.

    Args:
        my_tuple (tuple): A tuple of (value, key) tuples

    Returns:
        Dict: A dictionary mapping each tuple key to its value.

    """

    return dict((y, x) for x, y in my_tuple)
