#!/usr/bin/python3
"""Unittests for to_json_string and save_to_file."""
import json
import os
import tempfile
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list gives an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_one_dictionary(self):
        """One dictionary gives a string with one item."""
        dictionary = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        result = Base.to_json_string([dictionary])
        self.assertIsInstance(result, str)
        self.assertEqual(json.loads(result), [dictionary])

    def test_uses_double_quotes(self):
        """The result is real JSON, with double quotes."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_two_dictionaries(self):
        """Two dictionaries keep their order."""
        dictionaries = [{"id": 1, "width": 2}, {"id": 3, "width": 4}]
        result = Base.to_json_string(dictionaries)
        self.assertEqual(json.loads(result), dictionaries)

    def test_empty_result_is_a_string(self):
        """The result for no data is a string and not a list."""
        self.assertIsInstance(Base.to_json_string(None), str)
        self.assertIsInstance(Base.to_json_string([]), str)

    def test_true_and_none_values(self):
        """JSON writes true and null, not Python names."""
        result = Base.to_json_string([{"a": True, "b": None}])
        self.assertEqual(result, '[{"a": true, "b": null}]')

    def test_is_a_static_method(self):
        """The method can be called on the class and on an instance."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base().to_json_string(None), "[]")

    def test_missing_argument(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file, run in a temporary folder."""

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

    def read(self, name):
        """Return the content of a file."""
        with open(name, "r") as file:
            return file.read()

    def test_rectangle_file_name_and_content(self):
        """The file is Rectangle.json and holds the dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(json.loads(self.read("Rectangle.json")),
                         [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
                          {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])

    def test_square_file_name_and_content(self):
        """The file is Square.json and holds the dictionaries."""
        Square.save_to_file([Square(5, 1, 2)])
        self.assertTrue(os.path.exists("Square.json"))
        self.assertFalse(os.path.exists("Rectangle.json"))
        self.assertEqual(json.loads(self.read("Square.json")),
                         [{"id": 1, "size": 5, "x": 1, "y": 2}])

    def test_none(self):
        """None writes an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_empty_list(self):
        """An empty list writes an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_none_for_square(self):
        """None writes an empty list in Square.json."""
        Square.save_to_file(None)
        self.assertEqual(self.read("Square.json"), "[]")

    def test_empty_list_for_square(self):
        """An empty list writes an empty list in Square.json."""
        Square.save_to_file([])
        self.assertEqual(self.read("Square.json"), "[]")

    def test_one_rectangle(self):
        """One rectangle gives a list with one dictionary."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(json.loads(self.read("Rectangle.json")),
                         [{"id": 1, "width": 1, "height": 2,
                           "x": 0, "y": 0}])

    def test_one_square(self):
        """One square gives a list with one dictionary."""
        Square.save_to_file([Square(1)])
        self.assertEqual(json.loads(self.read("Square.json")),
                         [{"id": 1, "size": 1, "x": 0, "y": 0}])

    def test_file_is_overwritten(self):
        """A second save replaces the first one."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6, id=9)])
        content = json.loads(self.read("Rectangle.json"))
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]["id"], 9)

    def test_file_is_overwritten_with_empty_list(self):
        """Saving None after a real save leaves an empty list."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_content_is_one_json_string(self):
        """The file holds a JSON string made by to_json_string."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertEqual(self.read("Rectangle.json"),
                         Base.to_json_string([r.to_dictionary()]))

    def test_other_files_are_not_changed(self):
        """Saving rectangles does not touch Square.json."""
        Square.save_to_file([Square(3)])
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(len(json.loads(self.read("Square.json"))), 1)

    def test_missing_argument(self):
        """The list is required."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_returns_none(self):
        """The method returns nothing."""
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))


if __name__ == "__main__":
    unittest.main()
