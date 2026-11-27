#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module defines matrix_divided(matrix, div), which returns a new
matrix with every element divided by div and rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div.

    matrix must be a list of lists of integers or floats, all rows
    having the same size. div must be a non-zero number.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
