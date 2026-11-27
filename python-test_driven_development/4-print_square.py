#!/usr/bin/python3
"""Module that defines a function to print a square.

The function print_square prints a square with the character #.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the length of a side of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
