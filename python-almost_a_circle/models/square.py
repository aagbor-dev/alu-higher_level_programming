#!/usr/bin/python3
"""Defines the Square class, which inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with the same width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Create a square.

        Args:
            size (int): the size of the square, used as width and height.
            x (int): the horizontal position, 0 or more.
            y (int): the vertical position, 0 or more.
            id (int): the id of the instance, passed to the Base class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
