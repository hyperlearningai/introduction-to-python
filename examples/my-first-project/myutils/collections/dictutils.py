#!/usr/bin/env python3
"""Collection of useful tools for working with dictionary objects.

This module demonstrates the creation and usage of modules in Python.
The documentation standard for modules is to provide a docstring at the top
of the module script file. This docstring consists of a one-line summary
followed by a more detailed description of the module. Sections may also be
included in module docstrings, and are created with a section header and a
colon followed by a block of indented text. Refer to
https://www.python.org/dev/peps/pep-0008/ for the PEP 8 style guide for
Python code for further information.

"""

import pandas as pd


def convert_to_dataframe(my_dict, column_list):
    """Convert a given dictionary to a Pandas DataFrame.

    Args:
        my_dict (dictionary): The dictionary to convert to a DataFrame
        column_list (list): A list containing ordered column names

    Returns:
        DataFrame: Pandas DataFrame loaded with the given dictionary

    """

    return pd.DataFrame.from_dict(
        my_dict, orient='index', columns=column_list)
