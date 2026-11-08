#!/usr/bin/python3
"""Defines a function that checks for a subclass instance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    An object that is exactly an instance of a_class gives False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
