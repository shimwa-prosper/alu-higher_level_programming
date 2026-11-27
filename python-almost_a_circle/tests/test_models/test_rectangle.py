#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleConstructor(unittest.TestCase):
    """Test cases for the Rectangle constructor."""

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_width_height(self):
        """Rectangle(1, 2) sets width, height and default x, y."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_with_x(self):
        """Rectangle(1, 2, 3) sets x."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.x, r.y), (3, 0))

    def test_with_x_y(self):
        """Rectangle(1, 2, 3, 4) sets x and y."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.x, r.y), (3, 4))

    def test_with_id(self):
        """Rectangle(1, 2, 3, 4, 5) sets the id."""
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_auto_id_increments(self):
        """Ids continue from the Base counter."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_setters(self):
        """Setters change the attributes."""
        r = Rectangle(1, 2)
        r.width, r.height, r.x, r.y = 5, 6, 7, 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_attributes_are_private(self):
        """The raw names are not public attributes."""
        r = Rectangle(1, 2)
        self.assertEqual(r.__dict__["_Rectangle__width"], 1)

    def test_missing_args(self):
        """width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)


if __name__ == "__main__":
    unittest.main()
