#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def printed(function):
    """Return everything that a function prints."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        function()
    return buffer.getvalue()


class TestSquareInstance(unittest.TestCase):
    """Tests for creating a Square."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """A Square is a Rectangle and a Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_size_only(self):
        """The size is the width and the height."""
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id), (1, 1, 0, 0, 1))

    def test_all_arguments(self):
        """Every argument is stored."""
        s = Square(5, 2, 3, 12)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 2, 3, 12))

    def test_keyword_arguments(self):
        """Arguments can be given by name."""
        s = Square(size=4, x=1, y=2, id=7)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id), (4, 4, 1, 2, 7))

    def test_ids_increase(self):
        """Each square without id gets the next id."""
        self.assertEqual([Square(1).id, Square(1).id, Square(1).id],
                         [1, 2, 3])

    def test_shares_counter_with_rectangle(self):
        """Squares and rectangles use the same counter."""
        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Square(1).id, 2)

    def test_fourth_argument_is_id(self):
        """The fourth argument is the id and is not validated."""
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_no_new_attributes(self):
        """A square has the attributes of a rectangle only."""
        self.assertEqual(
            set(vars(Square(3))),
            {"id", "_Rectangle__width", "_Rectangle__height",
             "_Rectangle__x", "_Rectangle__y"})

    def test_missing_size(self):
        """The size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_arguments(self):
        """More than four arguments is a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareValidation(unittest.TestCase):
    """Tests for the validation, which comes from Rectangle."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_size_not_integer(self):
        """A size that is not an integer is a TypeError."""
        for value in ("1", 1.5, None, True, [1], (1,), {}, {1}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^width must be an integer$"):
                    Square(value)

    def test_x_not_integer(self):
        """An x that is not an integer is a TypeError."""
        for value in ("2", 2.5, None, True):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^x must be an integer$"):
                    Square(1, value)

    def test_y_not_integer(self):
        """A y that is not an integer is a TypeError."""
        for value in ("3", 3.5, None, True):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^y must be an integer$"):
                    Square(1, 2, value)

    def test_negative_size(self):
        """A negative size is a ValueError."""
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Square(-1)

    def test_zero_size(self):
        """A size of 0 is a ValueError."""
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Square(0)

    def test_negative_x(self):
        """A negative x is a ValueError."""
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Square(1, -2)

    def test_negative_y(self):
        """A negative y is a ValueError."""
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            Square(1, 2, -3)

    def test_zero_position(self):
        """A position of 0 is valid."""
        s = Square(1, 0, 0)
        self.assertEqual((s.x, s.y), (0, 0))


class TestSquareMethods(unittest.TestCase):
    """Tests for the methods of a Square."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_str_examples(self):
        """The strings of the task examples."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")

    def test_str_all_different(self):
        """Every value is different, so a swap would be seen."""
        self.assertEqual(str(Square(4, 2, 1, 12)), "[Square] (12) 2/1 - 4")

    def test_str_with_given_id(self):
        """The id that is given is shown."""
        self.assertEqual(str(Square(3, 1, 3, id=7)), "[Square] (7) 1/3 - 3")

    def test_print_uses_str(self):
        """The print function shows the same string."""
        s = Square(2, 3, 4, 5)
        self.assertEqual(printed(lambda: print(s)), "[Square] (5) 3/4 - 2\n")

    def test_area_examples(self):
        """The areas of the task examples."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_area_of_one(self):
        """The smallest square has an area of 1."""
        self.assertEqual(Square(1).area(), 1)

    def test_display_without_position(self):
        """A square without position."""
        self.assertEqual(printed(Square(5).display), "#####\n" * 5)

    def test_display_with_x(self):
        """A square with an x."""
        self.assertEqual(printed(Square(2, 2).display), "  ##\n  ##\n")

    def test_display_with_x_and_y(self):
        """A square with an x and a y."""
        self.assertEqual(printed(Square(3, 1, 3).display),
                         "\n\n\n ###\n ###\n ###\n")

    def test_width_and_height_setters_still_validate(self):
        """The width and height setters of Rectangle still work."""
        s = Square(2)
        s.width = 5
        self.assertEqual(s.width, 5)
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            s.height = 0


if __name__ == "__main__":
    unittest.main()
