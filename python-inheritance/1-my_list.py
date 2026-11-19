#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A list that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
