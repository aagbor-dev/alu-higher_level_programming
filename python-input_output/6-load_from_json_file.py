#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the object stored as JSON in a text file.

    Args:
        filename: the path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
