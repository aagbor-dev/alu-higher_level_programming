#!/usr/bin/python3
"""Unittests for models/base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def setUp(self):
        """Reset the object counter before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove json files created by the tests"""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        self.assertEqual(Base(89).id, 89)

    def test_id_given_does_not_increment(self):
        Base(89)
        self.assertEqual(Base().id, 1)

    def test_nb_objects_private(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_one(self):
        s = Base.to_json_string([{'id': 12}])
        self.assertEqual(type(s), str)
        self.assertEqual(s, '[{"id": 12}]')

    def test_to_json_string_two(self):
        s = Base.to_json_string([{'id': 1}, {'id': 2}])
        self.assertEqual(s, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_one(self):
        lst = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(type(lst), list)
        self.assertEqual(lst, [{'id': 89}])

    def test_from_json_string_two(self):
        lst = Base.from_json_string('[{"id": 1}, {"id": 2}]')
        self.assertEqual(lst, [{'id': 1}, {'id': 2}])

    def test_json_round_trip(self):
        d = [Rectangle(10, 7, 2, 8, 1).to_dictionary()]
        self.assertEqual(Base.from_json_string(Base.to_json_string(d)), d)


if __name__ == "__main__":
    unittest.main()
