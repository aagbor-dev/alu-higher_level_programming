#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the characters written.

    The file is created if it does not exist and overwritten if it does.

    Args:
        filename: the path of the file to write.
        text: the string to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
