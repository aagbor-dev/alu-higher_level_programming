#!/usr/bin/python3
"""Defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists of integers.

    Args:
        n: the number of rows. An empty list is returned if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        previous = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(previous[j - 1] + previous[j])
        row.append(1)
        triangle.append(row)
    return triangle
