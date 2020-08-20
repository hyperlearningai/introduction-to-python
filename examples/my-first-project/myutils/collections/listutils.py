#!/usr/bin/env python3
"""Collection of useful tools for working with list objects.

This module demonstrates the creation and usage of modules in Python.
The documentation standard for modules is to provide a docstring at the top
of the module script file. This docstring consists of a one-line summary
followed by a more detailed description of the module. Sections may also be
included in module docstrings, and are created with a section header and a
colon followed by a block of indented text. Refer to
https://www.python.org/dev/peps/pep-0008/ for the PEP 8 style guide for
Python code for further information.

"""


def convert_to_dict(my_keys, my_values):
    """Merge a given list of keys and a list of values into a dictionary.

    Args:
        my_keys (list): A list of keys
        my_values (list): A list corresponding values

    Returns:
        Dict: Dictionary of the list of keys mapped to the list of values

    """

    return dict(zip(my_keys, my_values))
