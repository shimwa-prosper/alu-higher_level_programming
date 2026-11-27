#!/usr/bin/python3
"""Module that adds two integers.

This module defines add_integer(a, b=98), which casts floats to
integers and returns the sum of the two numbers.
"""


def add_integer(a, b=98):
    """Return the sum of a and b after casting them to integers.
    Raise TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
