#!/usr/bin/python3
"""this test module fo testing on storage file"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """this test class fo testing on storage file"""

    def test_file_path(self):
        """check if file path is correct"""
        file_strg = FileStorage()
        self.assertEqual(file_strg.file_path, "file.json")

    def test_all(self):
        """this method for check if all function is getting
        the object tha we created"""
        base = BaseModel()
        file_strg = FileStorage()
        base.save()
        key = f"{base.__class__.__name__}.{base.id}"
        self.assertEqual(file_strg.all()[key], base)

    def test_new(self):
        """method for check if the new object is ctored in object dictionary
        waiting to store it in the file"""
        base = BaseModel()
        file_strg = FileStorage()
        file_strg.new(base)
        key = f"{base.__class__.__name__}.{base.id}"
        self.assertEqual(file_strg.all()[key], base)

    def test_save(self):
        """this method to chech if the new object that we created is
        exist in the file"""
        base = BaseModel()
        file_strg = FileStorage()
        file_strg.new(base)
        file_strg.save()
        key = f"{base.__class__.__name__}.{base.id}"
        try:
            with open("file.json", "r") as f:
                json_data = json.load(f)
            found = None
            for key_obj in json_data.keys():
                if key_obj == key:
                    found = key_obj
            self.assertEqual(found, key)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
