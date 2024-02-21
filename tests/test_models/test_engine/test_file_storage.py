#!/usr/bin/python3
"""unittest for FileStorage"""


import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_file_path(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        initial_count = len(self.storage.all())
        new_model = BaseModel()
        self.storage.new(new_model)
        new_count = len(self.storage.all())
        self.assertEqual(new_count, initial_count + 1)

    def test_save(self):
        self.model.name = "Test Model"
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = json.load(f)
            key = f"BaseModel.{self.model.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]["name"], "Test Model")

    def test_reload(self):
        self.assertTrue(len(self.storage.all()) > 0)
        self.model.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        key = f"BaseModel.{self.model.id}"
        data[key]['custom_attribute'] = "Test Reload"
        with open("file.json", "w") as f:
            json.dump(data, f)
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(key, all_objects)
        loaded_model = all_objects[key]
        self.assertTrue('custom_attribute' in loaded_model.to_dict())
        self.assertEqual(loaded_model.to_dict()['custom_attribute'], "Test Reload")

if __name__ == "__main__":
    unittest.main()