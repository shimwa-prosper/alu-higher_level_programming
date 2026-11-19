#!/usr/bin/python3
"""Define a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
