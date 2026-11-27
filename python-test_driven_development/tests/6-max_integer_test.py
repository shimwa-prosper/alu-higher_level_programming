#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        """Max at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning of the list."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        """Max in the middle of a longer list."""
        self.assertEqual(max_integer([1, 2, 99, 4, 5]), 99)

    def test_one_element(self):
        """List with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """No argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """List of only negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """List with negative, zero and positive numbers."""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_duplicates(self):
        """Repeated max value."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_floats(self):
        """List of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """Mix of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Very large integers."""
        self.assertEqual(max_integer([10**20, 10**19]), 10**20)

    def test_tuple(self):
        """A tuple works because it supports len and indexing."""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_string(self):
        """A string returns its biggest character."""
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        """A list of strings returns the biggest string."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_of_lists(self):
        """A list of lists compares them item by item."""
        self.assertEqual(max_integer([[1, 2], [3]]), [3])

    def test_none_raises(self):
        """None has no len, so it raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_raises(self):
        """An integer has no len, so it raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_mixed_types_raise(self):
        """Comparing a string and an int raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])


if __name__ == "__main__":
    unittest.main()
