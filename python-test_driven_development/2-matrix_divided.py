#!/usr/bin/python3
"""Module for matrix_divided.

This module defines a function that divides all the elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Args:
        matrix: a list of lists of integers or floats, all rows the same size.
        div: a number (integer or float) that is not 0.

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats,
            if the rows differ in size, or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(message)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError(message)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(number / div, 2) for number in row] for row in matrix]
