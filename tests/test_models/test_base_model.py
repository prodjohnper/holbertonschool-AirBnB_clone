#!/usr/bin/python3
"""Unittest for base_model"""


import unittest
from models.base_model import BaseModel
import uuid
import datetime

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        my_model = BaseModel()
        updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated_at, my_model.updated_at)
        self.assertFalse(my_model.updated_at is datetime)

    def test_to_dict(self):
        my_model = BaseModel()
        dict = my_model.to_dict()
        my_keys = {"__class__", "created_at", "updated_at", "id"}
        self.assertEqual(dict.keys(), my_keys)

    def test_id(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertTrue(uuid.UUID(my_model.id)) 

    def test_created_at(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime.datetime)

    def test_str(self):
        my_model = BaseModel()
        my_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), my_str)

if __name__ == '__main__':
    unittest.main()
