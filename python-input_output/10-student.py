#!/usr/bin/python3
"""Defines a class Student with a filtered dictionary description."""


class Student:
    """A student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Set the public attributes of the student.

        Args:
            first_name: the first name.
            last_name: the last name.
            age: the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the student.

        Args:
            attrs: an optional list of attribute names (strings). If it is
                given, only those attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
