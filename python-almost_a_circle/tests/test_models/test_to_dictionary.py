#!/usr/bin/python3
"""Unittests for the to_dictionary methods."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_all_values(self):
        """The dictionary holds id, width, height, x and y."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_default_position(self):
        """The position is 0 and 0 by default."""
        self.assertEqual(Rectangle(1, 1).to_dictionary(),
                         {"id": 1, "width": 1, "height": 1, "x": 0, "y": 0})

    def test_given_id(self):
        """A given id is in the dictionary."""
        self.assertEqual(Rectangle(3, 4, 5, 6, 77).to_dictionary(),
                         {"id": 77, "width": 3, "height": 4, "x": 5, "y": 6})

    def test_is_a_dict(self):
        """The result is a dictionary."""
        self.assertIs(type(Rectangle(1, 1).to_dictionary()), dict)

    def test_follows_changes(self):
        """The dictionary uses the current values."""
        r = Rectangle(1, 1)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.to_dictionary(),
                         {"id": 5, "width": 6, "height": 7, "x": 8, "y": 9})

    def test_changing_the_dictionary_keeps_the_object(self):
        """The dictionary is a copy, not the attributes themselves."""
        r = Rectangle(2, 3, 4, 5, 6)
        dictionary = r.to_dictionary()
        dictionary["width"] = 100
        self.assertEqual(r.width, 2)
        self.assertEqual(r.to_dictionary()["width"], 2)

    def test_update_with_the_dictionary(self):
        """The dictionary can be given back to update."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertIsNot(r1, r2)

    def test_takes_no_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_all_values(self):
        """The dictionary holds id, size, x and y."""
        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_default_position(self):
        """The position is 0 and 0 by default."""
        self.assertEqual(Square(4).to_dictionary(),
                         {"id": 1, "size": 4, "x": 0, "y": 0})

    def test_no_width_or_height(self):
        """The dictionary has no width and no height."""
        keys = set(Square(4).to_dictionary())
        self.assertEqual(keys, {"id", "size", "x", "y"})

    def test_given_id(self):
        """A given id is in the dictionary."""
        self.assertEqual(Square(3, 4, 5, 77).to_dictionary(),
                         {"id": 77, "size": 3, "x": 4, "y": 5})

    def test_is_a_dict(self):
        """The result is a dictionary."""
        self.assertIs(type(Square(1).to_dictionary()), dict)

    def test_follows_changes(self):
        """The dictionary uses the current values."""
        s = Square(1)
        s.update(5, 6, 7, 8)
        self.assertEqual(s.to_dictionary(),
                         {"id": 5, "size": 6, "x": 7, "y": 8})

    def test_update_with_the_dictionary(self):
        """The dictionary can be given back to update."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertIsNot(s1, s2)

    def test_takes_no_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
