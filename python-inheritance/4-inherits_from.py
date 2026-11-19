#!/usr/bin/python3
"""Define a function that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a strict subclass of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
