#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the x offset of the rectangle.
            y (int): the y offset of the rectangle.
            id (int): the id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get the x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x offset of the rectangle."""
        self.__x = value

    @property
    def y(self):
        """Get the y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y offset of the rectangle."""
        self.__y = value
