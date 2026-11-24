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

    @property
    def size(self):
        """Get or set the size of the square (its width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign values to the attributes of the square.

        Args:
            *args: the new values, in the order id, size, x, y.
            **kwargs: the new values by name. Ignored if args is not empty.
        """
        names = ("id", "size", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
