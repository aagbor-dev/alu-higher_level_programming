#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstance(unittest.TestCase):
    """Tests for creating a Rectangle and its id."""

    def setUp(self):
        """Reset the id counter so every test starts from 0."""
        Base._Base__nb_objects = 0

    def test_is_a_base(self):
        """A Rectangle is a Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_ids(self):
        """The ids follow the example of the task."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual([r1.id, r2.id, r3.id], [1, 2, 12])

    def test_rectangle_and_base_share_ids(self):
        """Rectangles and bases use the same counter."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Rectangle(1, 1).id, 2)

    def test_default_position(self):
        """The position is 0, 0 by default."""
        rectangle = Rectangle(3, 4)
        self.assertEqual((rectangle.x, rectangle.y), (0, 0))

    def test_all_arguments(self):
        """Every argument is stored."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_keyword_arguments(self):
        """Arguments can be given by name."""
        r = Rectangle(width=5, height=6, x=7, y=8, id=9)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (5, 6, 7, 8, 9))

    def test_id_none(self):
        """An id of None uses the counter."""
        self.assertEqual(Rectangle(1, 1, 0, 0, None).id, 1)

    def test_missing_arguments(self):
        """The width and the height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_arguments(self):
        """More than five arguments is a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_attributes(self):
        """The attributes are private."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.__dict__["_Rectangle__width"], 1)
        self.assertEqual(r.__dict__["_Rectangle__height"], 2)
        self.assertEqual(r.__dict__["_Rectangle__x"], 3)
        self.assertEqual(r.__dict__["_Rectangle__y"], 4)
        self.assertNotIn("width", r.__dict__)

    def test_big_numbers(self):
        """Big integers are accepted."""
        r = Rectangle(10 ** 20, 10 ** 20, 10 ** 20, 10 ** 20)
        self.assertEqual(r.area(), 10 ** 40)


class TestRectangleSetters(unittest.TestCase):
    """Tests for the getters and setters of a Rectangle."""

    def setUp(self):
        """Reset the id counter and make a rectangle."""
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 2)

    def test_set_width(self):
        """The width can be changed."""
        self.r.width = 20
        self.assertEqual(self.r.width, 20)

    def test_set_height(self):
        """The height can be changed."""
        self.r.height = 30
        self.assertEqual(self.r.height, 30)

    def test_set_x(self):
        """The x position can be changed."""
        self.r.x = 4
        self.assertEqual(self.r.x, 4)

    def test_set_y(self):
        """The y position can be changed."""
        self.r.y = 5
        self.assertEqual(self.r.y, 5)

    def test_set_x_and_y_to_zero(self):
        """The position can be 0."""
        self.r.x = 0
        self.r.y = 0
        self.assertEqual((self.r.x, self.r.y), (0, 0))

    def test_failed_set_keeps_old_value(self):
        """A rejected value does not change the attribute."""
        with self.assertRaises(ValueError):
            self.r.width = -1
        self.assertEqual(self.r.width, 10)
        with self.assertRaises(TypeError):
            self.r.height = "a"
        self.assertEqual(self.r.height, 2)

    def test_id_can_change(self):
        """The id is public and can be changed."""
        self.r.id = 77
        self.assertEqual(self.r.id, 77)


class TestRectangleValidation(unittest.TestCase):
    """Tests for the validation of the attributes."""

    BAD_TYPES = ["2", 2.5, None, True, False, [1], (1,), {}, {1}, 1j]

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_width_type(self):
        """A width that is not an integer is a TypeError."""
        for value in self.BAD_TYPES:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^width must be an integer$"):
                    Rectangle(value, 2)

    def test_height_type(self):
        """A height that is not an integer is a TypeError."""
        for value in self.BAD_TYPES:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^height must be an integer$"):
                    Rectangle(10, value)

    def test_x_type(self):
        """An x that is not an integer is a TypeError."""
        for value in self.BAD_TYPES:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^x must be an integer$"):
                    Rectangle(10, 2, value)

    def test_y_type(self):
        """A y that is not an integer is a TypeError."""
        for value in self.BAD_TYPES:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^y must be an integer$"):
                    Rectangle(10, 2, 3, value)

    def test_width_value(self):
        """A width of 0 or less is a ValueError."""
        for value in (0, -1, -10 ** 10):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        ValueError, "^width must be > 0$"):
                    Rectangle(value, 2)

    def test_height_value(self):
        """A height of 0 or less is a ValueError."""
        for value in (0, -1, -10 ** 10):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        ValueError, "^height must be > 0$"):
                    Rectangle(10, value)

    def test_x_value(self):
        """An x under 0 is a ValueError."""
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Rectangle(10, 2, -1)

    def test_y_value(self):
        """A y under 0 is a ValueError."""
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            Rectangle(10, 2, 3, -1)

    def test_setter_errors(self):
        """The setters validate like the constructor."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "^x must be an integer$"):
            r.x = {}
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            r.height = 0
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            r.y = -3

    def test_task_examples(self):
        """The four examples of the task give the expected messages."""
        cases = [
            (lambda: Rectangle(10, "2"), TypeError,
             "height must be an integer"),
            (lambda: setattr(Rectangle(10, 2), "width", -10), ValueError,
             "width must be > 0"),
            (lambda: setattr(Rectangle(10, 2), "x", {}), TypeError,
             "x must be an integer"),
            (lambda: Rectangle(10, 2, 3, -1), ValueError,
             "y must be >= 0"),
        ]
        for call, error, message in cases:
            with self.subTest(message=message):
                with self.assertRaises(error) as context:
                    call()
                self.assertEqual(str(context.exception), message)

    def test_width_checked_first(self):
        """When several values are wrong, the width is reported first."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            Rectangle("a", "b", "c", "d")

    def test_type_before_value(self):
        """The type is checked before the value."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            Rectangle("-1", 2)


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_area_examples(self):
        """The areas of the task examples are 6, 20 and 56."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_of_one(self):
        """The smallest rectangle has an area of 1."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_follows_changes(self):
        """The area uses the current width and height."""
        r = Rectangle(2, 3)
        r.width = 10
        r.height = 5
        self.assertEqual(r.area(), 50)

    def test_area_ignores_position(self):
        """The position does not change the area."""
        self.assertEqual(Rectangle(2, 3, 9, 9).area(), 6)

    def test_area_takes_no_argument(self):
        """The area method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(2, 3).area(5)


if __name__ == "__main__":
    unittest.main()
