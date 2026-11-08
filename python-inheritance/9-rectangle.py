#!/usr/bin/python3
"""Defines a class Rectangle with an area and a description."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a private width and height."""

    def __init__(self, width, height):
        """Set the width and height after validating them.

        Args:
            width: the width, a positive integer.
            height: the height, a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
