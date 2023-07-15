#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        tt = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(tt))
        self.assertNotIn("name", tt.__dict__)

    def test_two_states_unique_ids(self):
        tt1 = State()
        tt2 = State()
        self.assertNotEqual(tt1.id, tt2.id)

    def test_two_states_different_created_at(self):
        tt1 = State()
        sleep(0.05)
        tt2 = State()
        self.assertLess(tt1.created_at, tt2.created_at)

    def test_two_states_different_updated_at(self):
        tt1 = State()
        sleep(0.05)
        tt2 = State()
        self.assertLess(tt1.updated_at, tt2.updated_at)

    def test_str_representation(self):
        tds = datetime.today()
        dt_repr = repr(tds)
        tt = State()
        tt.id = "123456"
        tt.created_at = tt.updated_at = tds
        ttstr = tt.__str__()
        self.assertIn("[State] (123456)", ttstr)
        self.assertIn("'id': '123456'", ttstr)
        self.assertIn("'created_at': " + dt_repr, ttstr)
        self.assertIn("'updated_at': " + dt_repr, ttstr)

    def test_args_unused(self):
        tt = State(None)
        self.assertNotIn(None, tt.__dict__.values())

    def test_instantiation_with_kwargs(self):
        tds = datetime.today()
        dt_iso = tds.isoformat()
        tt = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(tt.id, "345")
        self.assertEqual(tt.created_at, tds)
        self.assertEqual(tt.updated_at, tds)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        tt = State()
        sleep(0.05)
        first_updated_at = tt.updated_at
        tt.save()
        self.assertLess(first_updated_at, tt.updated_at)

    def test_two_saves(self):
        tt = State()
        sleep(0.05)
        first_updated_at = tt.updated_at
        tt.save()
        second_updated_at = tt.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        tt.save()
        self.assertLess(second_updated_at, tt.updated_at)

    def test_save_with_arg(self):
        tt = State()
        with self.assertRaises(TypeError):
            tt.save(None)

    def test_save_updates_file(self):
        tt = State()
        tt.save()
        ttid = "State." + tt.id
        with open("file.json", "r") as f:
            self.assertIn(ttid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        tt = State()
        self.assertIn("id", tt.to_dict())
        self.assertIn("created_at", tt.to_dict())
        self.assertIn("updated_at", tt.to_dict())
        self.assertIn("__class__", tt.to_dict())

    def test_to_dict_contains_added_attributes(self):
        tt = State()
        tt.middle_name = "Holberton"
        tt.my_number = 98
        self.assertEqual("Holberton", tt.middle_name)
        self.assertIn("my_number", tt.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        tt = State()
        tt_dict = tt.to_dict()
        self.assertEqual(str, type(tt_dict["id"]))
        self.assertEqual(str, type(tt_dict["created_at"]))
        self.assertEqual(str, type(tt_dict["updated_at"]))

    def test_to_dict_output(self):
        tds = datetime.today()
        tt = State()
        tt.id = "123456"
        tt.created_at = tt.updated_at = tds
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': tds.isoformat(),
            'updated_at': tds.isoformat(),
        }
        self.assertDictEqual(tt.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        tt = State()
        self.assertNotEqual(tt.to_dict(), tt.__dict__)

    def test_to_dict_with_arg(self):
        tt = State()
        with self.assertRaises(TypeError):
            tt.to_dict(None)


if __name__ == "__main__":
    unittest.main()

