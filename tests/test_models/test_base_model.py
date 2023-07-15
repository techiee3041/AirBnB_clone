#!/usr/bin/python3
import models
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the BaseModel class."""

    def test_instantiation_without_arguments(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids_for_two_models(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_different_created_at_for_two_models(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_different_updated_at_for_two_models(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_string_representation(self):
        current_time = datetime.today()
        current_time_repr = repr(current_time)
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = current_time
        model_str = model.__str__()
        self.assertIn("[BaseModel] (123456)", model_str)
        self.assertIn("'id': '123456'", model_str)
        self.assertIn("'created_at': " + current_time_repr, model_str)
        self.assertIn("'updated_at': " + current_time_repr, model_str)

    def test_unused_args(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        current_time = datetime.today()
        current_time_iso = current_time.isoformat()
        model = BaseModel(id="345", created_at=current_time_iso, updated_at=current_time_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, current_time)
        self.assertEqual(model.updated_at, current_time)

    def test_instantiation_with_args_and_kwargs(self):
        current_time = datetime.today()
        current_time_iso = current_time.isoformat()
        model = BaseModel("12", id="345", created_at=current_time_iso, updated_at=current_time_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, current_time)
        self.assertEqual(model.updated_at, current_time)


class TestBaseModelSave(unittest.TestCase):
    """Unit tests for testing save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        model = BaseModel()
        sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_multiple_saves(self):
        model = BaseModel()
        sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        second_updated_at = model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        model.save()
        self.assertLess(second_updated_at, model.updated_at)

    def test_save_with_argument(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_save_updates_file(self):
        model = BaseModel()
        model.save()
        model_id = "BaseModel." + model.id
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unit tests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_to_dict_contains_added_attributes(self):
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 98
        self.assertIn("name", model.to_dict())
        self.assertIn("my_number", model.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_to_dict_output(self):
        current_time = datetime.today()
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = current_time
        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': current_time.isoformat(),
            'updated_at': current_time.isoformat()
        }
        self.assertDictEqual(model.to_dict(), expected_dict)

    def test_to_dict_differs_from_dunder_dict(self):
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_to_dict_with_argument(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == "__main__":
    unittest.main()
