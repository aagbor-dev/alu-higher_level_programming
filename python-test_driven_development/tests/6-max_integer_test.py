#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """The max is the last element of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The max is found in an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """The max is in the middle of the list."""
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument behaves like an empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """The max of negative numbers is the one closest to 0."""
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_negative_and_positive(self):
        """Negative and positive numbers can be mixed."""
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_all_equal(self):
        """A list of equal numbers returns that number."""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_duplicated_max(self):
        """The max can appear more than once."""
        self.assertEqual(max_integer([1, 9, 3, 9]), 9)

    def test_zero(self):
        """Zero is handled like any other number."""
        self.assertEqual(max_integer([0, 0]), 0)

    def test_floats(self):
        """Floats are compared like integers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_integers_and_floats(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Big numbers are handled."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 19]), 10 ** 20)

    def test_string_list(self):
        """Strings are compared alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_mixed_types(self):
        """Comparing a number and a string is a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none(self):
        """None instead of a list is a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_a_list(self):
        """An integer instead of a list is a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
