#!/usr/bin/python3
"""Module for add_integer.

This module defines a function that adds two integers.
The function casts floats to integers before adding them.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as an integer.
    Raises TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
