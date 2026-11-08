#!/usr/bin/python3
"""Defines a class Square with a private size."""


class Square:
    """A square with a private instance attribute size."""

    def __init__(self, size):
        """Set the size of the square.

        Args:
            size: the size of the square (no validation here).
        """
        self.__size = size
