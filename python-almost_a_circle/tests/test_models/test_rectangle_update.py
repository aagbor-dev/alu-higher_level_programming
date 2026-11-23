#!/usr/bin/python3
"""Unittests for the update method of Rectangle."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for update with no-keyword arguments."""

    def setUp(self):
        """Reset the id counter and make a rectangle."""
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 10, 10, 10)

    def values(self):
        """Return id, width, height, x and y of the rectangle."""
        r = self.r
        return (r.id, r.width, r.height, r.x, r.y)

    def test_no_argument(self):
        """Nothing changes without arguments."""
        self.r.update()
        self.assertEqual(self.values(), (1, 10, 10, 10, 10))

    def test_one_argument(self):
        """The first argument is the id."""
        self.r.update(89)
        self.assertEqual(self.values(), (89, 10, 10, 10, 10))

    def test_two_arguments(self):
        """The second argument is the width."""
        self.r.update(89, 2)
        self.assertEqual(self.values(), (89, 2, 10, 10, 10))

    def test_three_arguments(self):
        """The third argument is the height."""
        self.r.update(89, 2, 3)
        self.assertEqual(self.values(), (89, 2, 3, 10, 10))

    def test_four_arguments(self):
        """The fourth argument is x."""
        self.r.update(89, 2, 3, 4)
        self.assertEqual(self.values(), (89, 2, 3, 4, 10))

    def test_five_arguments(self):
        """The fifth argument is y."""
        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(self.values(), (89, 2, 3, 4, 5))

    def test_task_example(self):
        """The calls of the task give the strings of the task."""
        expected = [
            (lambda: self.r.update(89), "[Rectangle] (89) 10/10 - 10/10"),
            (lambda: self.r.update(89, 2), "[Rectangle] (89) 10/10 - 2/10"),
            (lambda: self.r.update(89, 2, 3), "[Rectangle] (89) 10/10 - 2/3"),
            (lambda: self.r.update(89, 2, 3, 4),
             "[Rectangle] (89) 4/10 - 2/3"),
            (lambda: self.r.update(89, 2, 3, 4, 5),
             "[Rectangle] (89) 4/5 - 2/3"),
        ]
        for call, text in expected:
            call()
            self.assertEqual(str(self.r), text)

    def test_more_than_five_arguments(self):
        """Arguments after the fifth are ignored."""
        self.r.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(self.values(), (1, 2, 3, 4, 5))

    def test_update_returns_none(self):
        """The update method returns nothing."""
        self.assertIsNone(self.r.update(1, 2))

    def test_invalid_width(self):
        """The new width is validated."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            self.r.update(89, "2")
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            self.r.update(89, 0)

    def test_invalid_height(self):
        """The new height is validated."""
        with self.assertRaisesRegex(TypeError, "^height must be an integer$"):
            self.r.update(89, 2, 2.5)
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            self.r.update(89, 2, -3)

    def test_invalid_x(self):
        """The new x is validated."""
        with self.assertRaisesRegex(TypeError, "^x must be an integer$"):
            self.r.update(89, 2, 3, None)
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            self.r.update(89, 2, 3, -4)

    def test_invalid_y(self):
        """The new y is validated."""
        with self.assertRaisesRegex(TypeError, "^y must be an integer$"):
            self.r.update(89, 2, 3, 4, [5])
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            self.r.update(89, 2, 3, 4, -5)

    def test_zero_is_valid_for_x_and_y(self):
        """The position can be set to 0."""
        self.r.update(1, 2, 3, 0, 0)
        self.assertEqual(self.values(), (1, 2, 3, 0, 0))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for update with key-worded arguments."""

    def setUp(self):
        """Reset the id counter and make a rectangle."""
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 10, 10, 10)

    def values(self):
        """Return id, width, height, x and y of the rectangle."""
        r = self.r
        return (r.id, r.width, r.height, r.x, r.y)

    def test_id_only(self):
        """The id can be set by name."""
        self.r.update(id=89)
        self.assertEqual(self.values(), (89, 10, 10, 10, 10))

    def test_width_only(self):
        """The width can be set by name."""
        self.r.update(width=1)
        self.assertEqual(self.values(), (1, 1, 10, 10, 10))

    def test_height_only(self):
        """The height can be set by name."""
        self.r.update(height=1)
        self.assertEqual(self.values(), (1, 10, 1, 10, 10))

    def test_x_only(self):
        """The x can be set by name."""
        self.r.update(x=2)
        self.assertEqual(self.values(), (1, 10, 10, 2, 10))

    def test_y_only(self):
        """The y can be set by name."""
        self.r.update(y=3)
        self.assertEqual(self.values(), (1, 10, 10, 10, 3))

    def test_several_names(self):
        """Several names at once."""
        self.r.update(width=1, x=2)
        self.assertEqual(self.values(), (1, 1, 10, 2, 10))

    def test_all_names_in_any_order(self):
        """The order of the names does not matter."""
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.values(), (89, 2, 10, 3, 1))
        self.r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.values(), (89, 4, 2, 1, 3))

    def test_task_example(self):
        """The calls of the task give the strings of the task."""
        self.r.update(height=1)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/1")
        self.r.update(width=1, x=2)
        self.assertEqual(str(self.r), "[Rectangle] (1) 2/10 - 1/1")
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 3/1 - 2/1")
        self.r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(self.r), "[Rectangle] (89) 1/3 - 4/2")

    def test_kwargs_skipped_when_args_exist(self):
        """The names are ignored if there are no-keyword arguments."""
        self.r.update(5, width=100, height=100, x=100, y=100)
        self.assertEqual(self.values(), (5, 10, 10, 10, 10))

    def test_kwargs_used_when_args_empty(self):
        """The names are used when there are no other arguments."""
        self.r.update(*[], width=7)
        self.assertEqual(self.values(), (1, 7, 10, 10, 10))

    def test_unknown_name_is_ignored(self):
        """A name that is not an attribute changes nothing."""
        self.r.update(color="red")
        self.assertEqual(self.values(), (1, 10, 10, 10, 10))
        self.assertFalse(hasattr(self.r, "color"))

    def test_known_and_unknown_names(self):
        """Known names are used even with an unknown one."""
        self.r.update(width=2, color="red")
        self.assertEqual(self.values(), (1, 2, 10, 10, 10))

    def test_invalid_values(self):
        """The values given by name are validated."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            self.r.update(width="1")
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            self.r.update(height=0)
        with self.assertRaisesRegex(TypeError, "^x must be an integer$"):
            self.r.update(x={})
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            self.r.update(y=-1)


if __name__ == "__main__":
    unittest.main()
