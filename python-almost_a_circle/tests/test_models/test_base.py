#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the id counter so every test starts from 0."""
        Base._Base__nb_objects = 0

    def test_first_id_is_one(self):
        """The first instance gets the id 1."""
        self.assertEqual(Base().id, 1)

    def test_ids_increase(self):
        """Each new instance gets the next id."""
        ids = [Base().id for _ in range(5)]
        self.assertEqual(ids, [1, 2, 3, 4, 5])

    def test_given_id(self):
        """An id that is given is used as it is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_move_counter(self):
        """A given id does not use up a number of the counter."""
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_task_example(self):
        """The example of the task gives 1, 2, 3, 12, 4."""
        ids = [Base().id, Base().id, Base().id, Base(12).id, Base().id]
        self.assertEqual(ids, [1, 2, 3, 12, 4])

    def test_given_id_zero(self):
        """The id 0 is a given id and is kept."""
        self.assertEqual(Base(0).id, 0)

    def test_given_negative_id(self):
        """A negative id is kept."""
        self.assertEqual(Base(-5).id, -5)

    def test_given_id_of_other_types(self):
        """The type of a given id is not checked."""
        for value in ("abc", 2.5, [1], (1,), {"a": 1}, True):
            with self.subTest(value=value):
                self.assertEqual(Base(value).id, value)

    def test_same_given_id_twice(self):
        """Two instances can have the same given id."""
        self.assertEqual(Base(7).id, Base(7).id)

    def test_none_id_uses_counter(self):
        """An id of None uses the counter."""
        self.assertEqual(Base(None).id, 1)

    def test_id_is_public(self):
        """The id can be read and changed."""
        base = Base()
        base.id = 99
        self.assertEqual(base.id, 99)

    def test_counter_is_private(self):
        """The counter is not reachable as a public attribute."""
        self.assertFalse(hasattr(Base, "nb_objects"))
        self.assertFalse(hasattr(Base, "__nb_objects"))

    def test_counter_value(self):
        """The private counter counts only the ids it created."""
        Base()
        Base(10)
        Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_instance_type(self):
        """An instance is a Base."""
        self.assertIsInstance(Base(), Base)

    def test_too_many_arguments(self):
        """More than one argument is a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_subclass_shares_counter(self):
        """A subclass uses the same counter."""

        class Child(Base):
            pass

        self.assertEqual([Base().id, Child().id, Base().id], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
