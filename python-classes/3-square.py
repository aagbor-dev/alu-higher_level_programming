#!/usr/bin/python3
"""Defines a class Square that can compute its area."""


class Square:
    """A square with a private, validated size and an area method."""

    def __init__(self, size=0):
        """Set the size of the square.

        Args:
            size: the size of the square, an integer >= 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
