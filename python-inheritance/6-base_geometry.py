#!/usr/bin/python3
"""Defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
