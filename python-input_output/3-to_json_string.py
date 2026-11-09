#!/usr/bin/python3
"""Defines a function that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object, as a string.

    Args:
        my_obj: the object to convert.
    """
    return json.dumps(my_obj)
