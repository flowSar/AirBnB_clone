#!/usr/bin/python3
"""test_base_models is dedicate to test base_model module
    and his has one unittst class and many function for testing
"""
import unittest
import json
from models.base_model import BaseModel
from datetime import datetime as dtime


class TestBaseModel(unittest.TestCase):
    """
        this is the class that was didicated for testing
        all BaseMode methods
    """
    def test_init(self):
        """test if the unite test qork is inteded for example
        check if updated_at != created_at
        """
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test__str__(self):
        """this test method is for magic method __str__ return"""
        base = BaseModel()
        base_str = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(base_str, base.__str__())

    def test_save(self):
        """this method for testing if the aboject that was create
            is stored in json file
        """
        base = BaseModel()
        base.save()
        found = False
        with open("file.json", "r") as f:
            jdata = json.load(f)
        for key in jdata.keys():
            obj_id = key.split(".")[1]
            if obj_id == base.id:
                found = True
        self.assertTrue(found)

    def test_to_dict(self):
        """this function test if the data that was generated by
            to_dict() method is the same data that was stored in json file
        """
        base = BaseModel()
        base.save()
        found = {}
        with open("file.json", "r") as f:
            jdata = json.load(f)
        for key in jdata.keys():
            obj_id = key.split(".")[1]
            if obj_id == base.id:
                found = jdata[key]
        self.assertEqual(found, base.to_dict())
        self.assertEqual(base.to_dict()['updated_at'], found['updated_at'])
        self.assertEqual(base.to_dict()['created_at'], found['created_at'])
        self.assertEqual(base.to_dict()['__class__'], found['__class__'])

if __name__ == '__main__':
    unittest.main()
