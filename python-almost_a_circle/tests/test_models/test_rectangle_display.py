#!/usr/bin/python3
"""Unittests for the display and __str__ methods of Rectangle."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


def printed(function):
    """Return everything that a function prints."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        function()
    return buffer.getvalue()


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_display_without_x_and_y(self):
        """With no position, there is no empty line and no space."""
        self.assertEqual(printed(Rectangle(4, 6).display),
                         "####\n" * 6)

    def test_display_small_without_x_and_y(self):
        """A 2 by 2 rectangle without position."""
        self.assertEqual(printed(Rectangle(2, 2).display), "##\n##\n")

    def test_display_one_by_one(self):
        """The smallest rectangle is a single character."""
        self.assertEqual(printed(Rectangle(1, 1).display), "#\n")

    def test_display_wide(self):
        """A rectangle wider than it is tall."""
        self.assertEqual(printed(Rectangle(5, 1).display), "#####\n")

    def test_display_tall(self):
        """A rectangle taller than it is wide."""
        self.assertEqual(printed(Rectangle(1, 3).display), "#\n#\n#\n")

    def test_display_with_x_and_y(self):
        """The y gives empty lines and the x gives spaces."""
        self.assertEqual(printed(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_without_y(self):
        """With only an x, there is no empty line."""
        self.assertEqual(printed(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_display_without_x(self):
        """With only a y, there is no space before the rows."""
        self.assertEqual(printed(Rectangle(2, 1, 0, 3).display),
                         "\n\n\n##\n")

    def test_display_big_position(self):
        """A bigger position."""
        self.assertEqual(printed(Rectangle(1, 2, 4, 3).display),
                         "\n\n\n    #\n    #\n")

    def test_display_uses_current_values(self):
        """The display follows changes of the attributes."""
        r = Rectangle(1, 1)
        r.width = 3
        r.height = 2
        r.x = 1
        r.y = 1
        self.assertEqual(printed(r.display), "\n ###\n ###\n")

    def test_display_does_not_change_attributes(self):
        """The display keeps x and y as they are."""
        r = Rectangle(2, 2)
        printed(r.display)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_display_returns_none(self):
        """The display prints and returns nothing."""
        with redirect_stdout(io.StringIO()):
            self.assertIsNone(Rectangle(1, 1).display())

    def test_display_takes_no_argument(self):
        """The display method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(5)


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_str_all_different(self):
        """Every value is different, so a swap would be seen."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_position(self):
        """The position is 0/0 by default."""
        self.assertEqual(str(Rectangle(10, 10, id=1)),
                         "[Rectangle] (1) 0/0 - 10/10")

    def test_str_uses_counter_id(self):
        """The id comes from the counter if it is not given."""
        self.assertEqual(str(Rectangle(5, 3)), "[Rectangle] (1) 0/0 - 5/3")
        self.assertEqual(str(Rectangle(5, 3)), "[Rectangle] (2) 0/0 - 5/3")

    def test_str_width_and_height_order(self):
        """The width comes before the height."""
        self.assertEqual(str(Rectangle(7, 8, 0, 0, 1)),
                         "[Rectangle] (1) 0/0 - 7/8")

    def test_str_x_and_y_order(self):
        """The x comes before the y."""
        self.assertEqual(str(Rectangle(1, 1, 3, 4, 1)),
                         "[Rectangle] (1) 3/4 - 1/1")

    def test_str_follows_changes(self):
        """The string uses the current values."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.width = 5
        r.height = 6
        r.x = 7
        r.y = 8
        r.id = 9
        self.assertEqual(str(r), "[Rectangle] (9) 7/8 - 5/6")

    def test_print_uses_str(self):
        """The print function shows the same string."""
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(printed(lambda: print(r)),
                         "[Rectangle] (6) 4/5 - 2/3\n")

    def test_str_returns_string(self):
        """The result is a string."""
        self.assertIsInstance(Rectangle(1, 1).__str__(), str)


if __name__ == "__main__":
    unittest.main()
