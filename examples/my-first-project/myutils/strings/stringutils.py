#!/usr/bin/env python3
"""Collection of useful tools for working with strings.

This module demonstrates the creation and usage of modules in Python.
The documentation standard for modules is to provide a docstring at the top
of the module script file. This docstring consists of a one-line summary
followed by a more detailed description of the module. Sections may also be
included in module docstrings, and are created with a section header and a
colon followed by a block of indented text. Refer to
https://www.python.org/dev/peps/pep-0008/ for the PEP 8 style guide for
Python code for further information.

"""

import re


def calc_word_frequency(my_string, my_word):
    """Calculate the number of occurrences of a given word in a given string.

    Args:
        my_string (str): String to search
        my_word (str): The word to search for

    Returns:
        int: The number of occurrences of the given word in the given string.

    """

    # Remove all non alphanumeric characters from the string
    filtered_string = re.sub(r'[^A-Za-z0-9 ]+', '', my_string)

    # Return the number of occurrences of my_word in the filtered string
    return filtered_string.split().count(my_word)
