#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """A square defined by its size."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of the square (no validation yet).
        """
        self.__size = size
