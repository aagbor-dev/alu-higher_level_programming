#!/usr/bin/python3
"""Module for text_indentation.

This module defines a function that prints a text with a gap after
each period, question mark and colon.
"""


def text_indentation(text):
    """Print text with 2 new lines after each of the characters . ? and :

    No space is printed at the beginning or the end of a printed line.

    Args:
        text: the text to print, a string.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")
