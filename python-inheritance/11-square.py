#!/usr/bin/python3
"""Defines a class Square with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a private size."""

    def __init__(self, size):
        """Set the size after validating it.

        Args:
            size: the size, a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
