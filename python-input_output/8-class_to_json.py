#!/usr/bin/python3
"""Module that defines the class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__.copy()
