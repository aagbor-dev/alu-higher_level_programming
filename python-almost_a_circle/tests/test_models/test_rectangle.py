#!/usr/bin/python3
"""Unittests for models/rectangle.py"""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def setUp(self):
        """Reset the object counter before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove json files created by the tests"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def capture(self, func):
        """Return what func prints to stdout"""
        with patch('sys.stdout', new=io.StringIO()) as out:
            func()
        return out.getvalue()

    # ----- instantiation -----
    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))
        self.assertEqual(r.id, 1)

    def test_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_auto_id(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_attributes(self):
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        with self.assertRaises(AttributeError):
            r.__height
        with self.assertRaises(AttributeError):
            r.__x
        with self.assertRaises(AttributeError):
            r.__y

    def test_setters(self):
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 20
        r.x = 3
        r.y = 4
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 3, 4))

    # ----- TypeError -----
    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2])

    def test_width_setter_str(self):
        r = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "5"

    # ----- ValueError -----
    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_x_y_zero_ok(self):
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_type_checked_before_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", -1)

    def test_width_checked_first(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", "invalid")

    # ----- area -----
    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_big(self):
        self.assertEqual(Rectangle(999, 999).area(), 998001)

    def test_area_after_change(self):
        r = Rectangle(2, 10)
        r.width = 8
        self.assertEqual(r.area(), 80)

    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(1)

    # ----- __str__ -----
    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_defaults(self):
        r = Rectangle(5, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 5/5")

    def test_str_print(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(self.capture(lambda: print(r)),
                         "[Rectangle] (12) 2/1 - 4/6\n")

    # ----- display -----
    def test_display_no_x_y(self):
        r = Rectangle(2, 3)
        self.assertEqual(self.capture(r.display), "##\n##\n##\n")

    def test_display_no_y(self):
        r = Rectangle(2, 2, 2)
        self.assertEqual(self.capture(r.display), "  ##\n  ##\n")

    def test_display_x_y(self):
        r = Rectangle(2, 3, 2, 2)
        self.assertEqual(self.capture(r.display),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_y_only(self):
        r = Rectangle(1, 1, 0, 1)
        self.assertEqual(self.capture(r.display), "\n#\n")

    # ----- to_dictionary -----
    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(r.to_dictionary(),
                         {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_to_dictionary_type(self):
        self.assertEqual(type(Rectangle(1, 2).to_dictionary()), dict)

    def test_to_dictionary_update(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    # ----- update *args -----
    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_args_1(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_args_2(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")

    def test_update_args_3(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")

    def test_update_args_4(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_args_5(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_args_invalid(self):
        r = Rectangle(10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "1")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_skip_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=7)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    # ----- update **kwargs -----
    def test_update_kwargs_1(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs_2(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")

    def test_update_kwargs_3(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")

    def test_update_kwargs_4(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_kwargs_5(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwargs_any_order(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_kwargs_invalid(self):
        r = Rectangle(10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)

    # ----- create -----
    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_with_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 1/2")

    def test_create_all(self):
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**d)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_new_object(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    # ----- save_to_file -----
    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                Base.from_json_string(f.read()),
                [{'id': 1, 'width': 1, 'height': 2, 'x': 0, 'y': 0}])

    def test_save_to_file_two(self):
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(Base.from_json_string(f.read())), 2)

    def test_save_to_file_overwrite(self):
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(Base.from_json_string(f.read())), 1)

    # ----- load_from_file -----
    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_empty(self):
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertTrue(all(type(o) is Rectangle for o in out))
        self.assertEqual(str(out[0]), str(r1))
        self.assertEqual(str(out[1]), str(r2))


if __name__ == "__main__":
    unittest.main()
