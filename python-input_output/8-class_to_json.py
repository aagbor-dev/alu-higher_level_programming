#!/usr/bin/python3
"""Defines a function that converts an object to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON.

    Args:
        obj: an instance of a class whose attributes are simple types.
    """
    return obj.__dict__
