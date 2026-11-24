#!/usr/bin/python3
"""Unittests for models/square.py"""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def setUp(self):
        """Reset the object counter before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove json files created by the tests"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def capture(self, func):
        """Return what func prints to stdout"""
        with patch('sys.stdout', new=io.StringIO()) as out:
            func()
        return out.getvalue()

    # ----- instantiation -----
    def test_is_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)
        self.assertIsInstance(Square(1), Base)

    def test_one_arg(self):
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 0, 0, 1))

    def test_two_args(self):
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_four_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_auto_id(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(s2.id, s1.id + 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_width_height_equal_size(self):
        s = Square(5)
        self.assertEqual((s.width, s.height), (5, 5))

    # ----- size getter / setter -----
    def test_size_getter(self):
        self.assertEqual(Square(5).size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))

    def test_size_setter_str(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_zero(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    # ----- TypeError -----
    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5)

    def test_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    # ----- ValueError -----
    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    # ----- area -----
    def test_area(self):
        self.assertEqual(Square(3).area(), 9)

    def test_area_after_change(self):
        s = Square(3)
        s.size = 4
        self.assertEqual(s.area(), 16)

    # ----- __str__ -----
    def test_str(self):
        self.assertEqual(str(Square(4, 2, 1, 12)),
                         "[Square] (12) 2/1 - 4")

    def test_str_defaults(self):
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")

    def test_str_print(self):
        s = Square(3, 1, 3, 7)
        self.assertEqual(self.capture(lambda: print(s)),
                         "[Square] (7) 1/3 - 3\n")

    # ----- display -----
    def test_display_no_x_y(self):
        self.assertEqual(self.capture(Square(2).display), "##\n##\n")

    def test_display_no_y(self):
        self.assertEqual(self.capture(Square(2, 2).display),
                         "  ##\n  ##\n")

    def test_display_x_y(self):
        self.assertEqual(self.capture(Square(2, 1, 2).display),
                         "\n\n ##\n ##\n")

    # ----- to_dictionary -----
    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        self.assertEqual(s.to_dictionary(),
                         {'id': 5, 'size': 10, 'x': 2, 'y': 1})

    def test_to_dictionary_type(self):
        self.assertEqual(type(Square(1).to_dictionary()), dict)

    def test_to_dictionary_update(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    # ----- update *args -----
    def test_update_no_args(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")

    def test_update_args_1(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_args_2(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 1")

    def test_update_args_3(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 2/10 - 1")

    def test_update_args_4(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_args_invalid(self):
        s = Square(10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "1")

    def test_update_args_skip_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, x=7)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")

    # ----- update **kwargs -----
    def test_update_kwargs_1(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89})
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_kwargs_2(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(s), "[Square] (89) 10/10 - 1")

    def test_update_kwargs_3(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s), "[Square] (89) 2/10 - 1")

    def test_update_kwargs_4(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_kwargs_any_order(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=7, id=89)
        self.assertEqual(str(s), "[Square] (89) 10/1 - 7")

    def test_update_kwargs_invalid(self):
        s = Square(10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    # ----- create -----
    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")

    def test_create_all(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_new_object(self):
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    # ----- save_to_file -----
    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(Base.from_json_string(f.read()),
                             [{'id': 1, 'size': 1, 'x': 0, 'y': 0}])

    def test_save_to_file_two(self):
        Square.save_to_file([Square(1), Square(2)])
        with open("Square.json", "r") as f:
            self.assertEqual(len(Base.from_json_string(f.read())), 2)

    # ----- load_from_file -----
    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty(self):
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertTrue(all(type(o) is Square for o in out))
        self.assertEqual(str(out[0]), str(s1))
        self.assertEqual(str(out[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
