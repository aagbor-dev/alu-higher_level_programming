#!/usr/bin/python3
"""Unittests for the size property and the update method of Square."""
import unittest
from models.base import Base
from models.square import Square


class TestSquareSize(unittest.TestCase):
    """Tests for the size getter and setter."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_get_size(self):
        """The size is the size given to the constructor."""
        self.assertEqual(Square(5).size, 5)

    def test_set_size(self):
        """The setter changes the width and the height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))

    def test_set_size_string(self):
        """The task example prints the new size."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        s.size = 10
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_follows_width(self):
        """The size is read from the width."""
        s = Square(5)
        s.width = 8
        self.assertEqual(s.size, 8)

    def test_size_not_integer(self):
        """A size that is not an integer is a TypeError about the width."""
        s = Square(5)
        for value in ("9", 9.5, None, True, [9], (9,), {}, {9}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^width must be an integer$"):
                    s.size = value
        self.assertEqual((s.width, s.height), (5, 5))

    def test_size_zero(self):
        """A size of 0 is a ValueError about the width."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            s.size = 0
        self.assertEqual(s.size, 5)

    def test_size_negative(self):
        """A negative size is a ValueError about the width."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            s.size = -3
        self.assertEqual(s.size, 5)

    def test_size_is_not_an_instance_attribute(self):
        """The size is a property and not a stored attribute."""
        self.assertNotIn("size", vars(Square(5)))
        self.assertIsInstance(Square.size, property)


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for update with no-keyword arguments."""

    def setUp(self):
        """Reset the id counter and make a square."""
        Base._Base__nb_objects = 0
        self.s = Square(5)

    def values(self):
        """Return id, size, x and y of the square."""
        s = self.s
        return (s.id, s.size, s.x, s.y)

    def test_no_argument(self):
        """Nothing changes without arguments."""
        self.s.update()
        self.assertEqual(self.values(), (1, 5, 0, 0))

    def test_one_argument(self):
        """The first argument is the id."""
        self.s.update(10)
        self.assertEqual(self.values(), (10, 5, 0, 0))

    def test_two_arguments(self):
        """The second argument is the size."""
        self.s.update(1, 2)
        self.assertEqual(self.values(), (1, 2, 0, 0))
        self.assertEqual((self.s.width, self.s.height), (2, 2))

    def test_three_arguments(self):
        """The third argument is x."""
        self.s.update(1, 2, 3)
        self.assertEqual(self.values(), (1, 2, 3, 0))

    def test_four_arguments(self):
        """The fourth argument is y."""
        self.s.update(1, 2, 3, 4)
        self.assertEqual(self.values(), (1, 2, 3, 4))

    def test_task_example(self):
        """The calls of the task give the strings of the task."""
        self.s.update(10)
        self.assertEqual(str(self.s), "[Square] (10) 0/0 - 5")
        self.s.update(1, 2)
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 2")
        self.s.update(1, 2, 3)
        self.assertEqual(str(self.s), "[Square] (1) 3/0 - 2")
        self.s.update(1, 2, 3, 4)
        self.assertEqual(str(self.s), "[Square] (1) 3/4 - 2")

    def test_more_than_four_arguments(self):
        """Arguments after the fourth are ignored."""
        self.s.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(self.values(), (1, 2, 3, 4))

    def test_update_returns_none(self):
        """The update method returns nothing."""
        self.assertIsNone(self.s.update(1, 2))

    def test_invalid_values(self):
        """The new values are validated."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            self.s.update(1, "2")
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            self.s.update(1, 0)
        with self.assertRaisesRegex(TypeError, "^x must be an integer$"):
            self.s.update(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            self.s.update(1, 2, -3)
        with self.assertRaisesRegex(TypeError, "^y must be an integer$"):
            self.s.update(1, 2, 3, None)
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            self.s.update(1, 2, 3, -4)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for update with key-worded arguments."""

    def setUp(self):
        """Reset the id counter and make a square."""
        Base._Base__nb_objects = 0
        self.s = Square(5)

    def values(self):
        """Return id, size, x and y of the square."""
        s = self.s
        return (s.id, s.size, s.x, s.y)

    def test_x_only(self):
        """The x can be set by name."""
        self.s.update(x=12)
        self.assertEqual(self.values(), (1, 5, 12, 0))

    def test_size_and_y(self):
        """The size and y can be set by name."""
        self.s.update(size=7, y=1)
        self.assertEqual(self.values(), (1, 7, 0, 1))
        self.assertEqual((self.s.width, self.s.height), (7, 7))

    def test_id_size_and_y(self):
        """The id, the size and y can be set by name."""
        self.s.update(size=7, id=89, y=1)
        self.assertEqual(self.values(), (89, 7, 0, 1))

    def test_task_example(self):
        """The calls of the task give the strings of the task."""
        self.s.update(x=12)
        self.assertEqual(str(self.s), "[Square] (1) 12/0 - 5")
        self.s.update(size=7, y=1)
        self.assertEqual(str(self.s), "[Square] (1) 12/1 - 7")
        self.s.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s), "[Square] (89) 12/1 - 7")

    def test_all_names_in_any_order(self):
        """The order of the names does not matter."""
        self.s.update(y=4, x=3, size=2, id=9)
        self.assertEqual(self.values(), (9, 2, 3, 4))

    def test_kwargs_skipped_when_args_exist(self):
        """The names are ignored if there are no-keyword arguments."""
        self.s.update(5, size=100, x=100, y=100)
        self.assertEqual(self.values(), (5, 5, 0, 0))

    def test_unknown_name_is_ignored(self):
        """A name that is not an attribute changes nothing."""
        self.s.update(color="red")
        self.assertEqual(self.values(), (1, 5, 0, 0))
        self.assertFalse(hasattr(self.s, "color"))

    def test_invalid_values(self):
        """The values given by name are validated."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            self.s.update(size="1")
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            self.s.update(x=-1)
        with self.assertRaisesRegex(TypeError, "^y must be an integer$"):
            self.s.update(y={})


if __name__ == "__main__":
    unittest.main()
