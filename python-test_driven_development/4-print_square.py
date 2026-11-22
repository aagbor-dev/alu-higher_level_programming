#!/usr/bin/python3
"""Module for print_square.

This module defines a function that prints a square with the character #.
"""


def print_square(size):
    """Print a square of size by size with the character #.

    Args:
        size: the length of a side, an integer that is 0 or more.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
