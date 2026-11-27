#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_id_automatic(self):
        """Base() gets an id automatically."""
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_id_increments(self):
        """Base() gets the previous id + 1."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        """Base(89) keeps the id passed."""
        self.assertEqual(Base(89).id, 89)

    def test_given_id_does_not_change_counter(self):
        """A given id does not use up an automatic id."""
        b1 = Base()
        Base(50)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)


if __name__ == "__main__":
    unittest.main()
