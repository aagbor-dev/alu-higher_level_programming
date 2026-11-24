#!/usr/bin/python3
"""Unittests for from_json_string, create and load_from_file."""
import json
import os
import tempfile
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_json_list(self):
        """The string [] gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_task_example(self):
        """The example of the task gives back the same list."""
        items = [{"id": 89, "width": 10, "height": 4},
                 {"id": 7, "width": 1, "height": 7}]
        text = Rectangle.to_json_string(items)
        result = Rectangle.from_json_string(text)
        self.assertIs(type(result), list)
        self.assertEqual(result, items)

    def test_one_item(self):
        """A string with one dictionary gives a list with one dictionary."""
        result = Base.from_json_string('[{"id": 1, "size": 2}]')
        self.assertEqual(result, [{"id": 1, "size": 2}])

    def test_values_keep_their_types(self):
        """Numbers, booleans and null come back as Python values."""
        result = Base.from_json_string('[{"a": 1, "b": true, "c": null}]')
        self.assertEqual(result, [{"a": 1, "b": True, "c": None}])

    def test_round_trip(self):
        """to_json_string and from_json_string undo each other."""
        items = [{"id": 1, "x": 2}, {"id": 3, "x": 4}]
        self.assertEqual(
            Base.from_json_string(Base.to_json_string(items)), items)

    def test_invalid_json(self):
        """A string that is not JSON is a ValueError."""
        with self.assertRaises(ValueError):
            Base.from_json_string("not json")

    def test_missing_argument(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestCreate(unittest.TestCase):
    """Tests for Base.create."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def rectangle_values(self, r):
        """Return id, width, height, x and y of a rectangle."""
        return (r.id, r.width, r.height, r.x, r.y)

    def test_rectangle_task_example(self):
        """The example of the task makes an equal but separate rectangle."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_rectangle_type(self):
        """The result is a Rectangle."""
        self.assertIs(type(Rectangle.create(id=1)), Rectangle)

    def test_rectangle_id_only(self):
        """With only an id, the dummy values stay."""
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(self.rectangle_values(r), (89, 1, 1, 0, 0))

    def test_rectangle_id_and_width(self):
        """The width is set."""
        r = Rectangle.create(**{"id": 89, "width": 2})
        self.assertEqual(self.rectangle_values(r), (89, 2, 1, 0, 0))

    def test_rectangle_up_to_height(self):
        """The height is set."""
        r = Rectangle.create(**{"id": 89, "width": 2, "height": 3})
        self.assertEqual(self.rectangle_values(r), (89, 2, 3, 0, 0))

    def test_rectangle_up_to_x(self):
        """The x is set."""
        r = Rectangle.create(**{"id": 89, "width": 2, "height": 3, "x": 4})
        self.assertEqual(self.rectangle_values(r), (89, 2, 3, 4, 0))

    def test_rectangle_all_values(self):
        """Every attribute is set."""
        r = Rectangle.create(
            **{"id": 89, "width": 2, "height": 3, "x": 4, "y": 5})
        self.assertEqual(self.rectangle_values(r), (89, 2, 3, 4, 5))

    def test_rectangle_without_id(self):
        """Without an id, the next free id is used."""
        r = Rectangle.create(width=2, height=3)
        self.assertEqual(self.rectangle_values(r), (1, 2, 3, 0, 0))

    def test_rectangle_is_validated(self):
        """Wrong values are rejected like in update."""
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            Rectangle.create(id=1, width="2")
        with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
            Rectangle.create(id=1, height=0)

    def test_square_id_only(self):
        """With only an id, the dummy values stay."""
        s = Square.create(**{"id": 89})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 0, 0))

    def test_square_id_and_size(self):
        """The size is set."""
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 0, 0))
        s = Square.create(**{"id": 89, "size": 5})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 5, 0, 0))

    def test_square_up_to_x(self):
        """The x is set."""
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 0))

    def test_square_all_values(self):
        """Every attribute is set."""
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_square_type(self):
        """The result is a Square."""
        self.assertIs(type(Square.create(id=1, size=2)), Square)

    def test_square_without_id(self):
        """Without an id, the next free id is used."""
        s = Square.create(size=4)
        self.assertEqual((s.id, s.size), (1, 4))

    def test_square_width_and_height_match(self):
        """The width and the height follow the size."""
        s = Square.create(id=1, size=6)
        self.assertEqual((s.width, s.height), (6, 6))

    def test_round_trip_with_to_dictionary(self):
        """create undoes to_dictionary."""
        s1 = Square(10, 2, 1)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_returns_new_object_each_time(self):
        """Two calls give two objects."""
        data = {"id": 1, "width": 2, "height": 3}
        self.assertIsNot(Rectangle.create(**data), Rectangle.create(**data))


class TestLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file, run in a temporary folder."""

    def setUp(self):
        """Reset the id counter and move to an empty temporary folder."""
        Base._Base__nb_objects = 0
        self.folder = tempfile.TemporaryDirectory()
        self.old_folder = os.getcwd()
        os.chdir(self.folder.name)

    def tearDown(self):
        """Go back to the old folder and remove the temporary one."""
        os.chdir(self.old_folder)
        self.folder.cleanup()

    def write(self, name, content):
        """Write a file in the temporary folder."""
        with open(name, "w") as file:
            file.write(content)

    def test_rectangle_file_missing(self):
        """A missing Rectangle.json gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_square_file_missing(self):
        """A missing Square.json gives an empty list."""
        self.assertEqual(Square.load_from_file(), [])

    def test_rectangles_round_trip(self):
        """Saved rectangles come back with the same values."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in result],
                         ["[Rectangle] (1) 2/8 - 10/7",
                          "[Rectangle] (2) 0/0 - 2/4"])
        for loaded in result:
            self.assertIs(type(loaded), Rectangle)

    def test_squares_round_trip(self):
        """Saved squares come back with the same values."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        result = Square.load_from_file()
        self.assertEqual([str(s) for s in result],
                         ["[Square] (1) 0/0 - 5", "[Square] (2) 9/1 - 7"])
        for loaded in result:
            self.assertIs(type(loaded), Square)

    def test_loaded_objects_are_new(self):
        """The loaded objects are not the saved ones."""
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        self.assertIsNot(Rectangle.load_from_file()[0], r1)

    def test_loaded_values_are_exact(self):
        """Every attribute of a loaded rectangle matches the file."""
        self.write("Rectangle.json", json.dumps(
            [{"id": 5, "width": 2, "height": 3, "x": 4, "y": 6}]))
        r = Rectangle.load_from_file()[0]
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (5, 2, 3, 4, 6))

    def test_empty_json_list(self):
        """A file with [] gives an empty list."""
        self.write("Rectangle.json", "[]")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_empty_file(self):
        """An empty file gives an empty list."""
        self.write("Square.json", "")
        self.assertEqual(Square.load_from_file(), [])

    def test_result_is_a_list(self):
        """The result is a list."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertIs(type(Rectangle.load_from_file()), list)

    def test_each_class_reads_its_own_file(self):
        """Rectangle does not read Square.json and the other way."""
        Square.save_to_file([Square(3)])
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(len(Square.load_from_file()), 1)
        self.assertEqual(len(Rectangle.load_from_file()), 1)

    def test_save_none_then_load(self):
        """A file saved from None loads as an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_many_objects(self):
        """A longer list keeps its order."""
        items = [Rectangle(i, i + 1, id=i) for i in range(1, 8)]
        Rectangle.save_to_file(items)
        ids = [r.id for r in Rectangle.load_from_file()]
        self.assertEqual(ids, [1, 2, 3, 4, 5, 6, 7])

    def test_takes_no_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)


if __name__ == "__main__":
    unittest.main()
