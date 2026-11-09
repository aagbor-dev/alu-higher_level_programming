#!/usr/bin/python3
"""Defines a function that saves an object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: the object to save.
        filename: the path of the file to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
