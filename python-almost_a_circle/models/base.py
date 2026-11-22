#!/usr/bin/python3
"""Defines the Base class, the base of all the other classes."""


class Base:
    """Manages the id attribute of all the other classes.

    Attributes:
        __nb_objects (int): the number of Base instances created so far.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Set the id of the new instance.

        Args:
            id (int): the id to use. If it is None, the next free id is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
