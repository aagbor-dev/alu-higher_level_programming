#!/usr/bin/python3
"""Defines a class Student."""


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

    def to_json(self):
        """Return the dictionary description of the student."""
        return self.__dict__
