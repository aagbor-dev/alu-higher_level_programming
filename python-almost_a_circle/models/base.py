#!/usr/bin/python3
"""Defines the Base class, the base of all the other classes."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries, or None.

        Returns:
            "[]" if list_dictionaries is None or empty, otherwise the
            JSON string of the list.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of instances to a file.

        The file is named <class name>.json and is overwritten if it
        already exists.

        Args:
            list_objs (list): a list of instances of a class that inherits
                from Base, or None.
        """
        if list_objs is None:
            list_objs = []
        dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dictionaries))
