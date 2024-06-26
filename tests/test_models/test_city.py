#!/usr/bin/python3
"""test_base_models is dedicate to test base_model module
    and his has one unittst class and many function for testing
"""
import unittest
import json
from models.city import City
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
        city = City()
        city.id = "1234567-1234567"
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)
        self.assertEqual(city.id, "1234567-1234567")

    def test_save(self):
        """this method for testing if the aboject that was create
            is stored in json file
        """
        city = City()
        city.id = "1234567-1234567"
        city.name = "name"
        city.save()
        found = False
        found_data = {}
        with open("file.json", "r") as f:
            jdata = json.load(f)
        for key in jdata.keys():
            obj_id = key.split(".")[1]
            if obj_id == city.id:
                found = True
                found_data = jdata[key]
        self.assertTrue(found)
        self.assertEqual(city.id, found_data["id"])
        self.assertEqual(city.name, found_data["name"])

    def test_to_dict(self):
        """this functio test if the data that was generated by
        to_dict() method is the same data that was stored in json file"""
        city = City()
        city.save()
        found = {}
        with open("file.json", "r") as f:
            jdata = json.load(f)
        for key in jdata.keys():
            obj_id = key.split(".")[1]
            if obj_id == city.id:
                found = jdata[key]
        self.assertEqual(found, city.to_dict())


if __name__ == '__main__':
    unittest.main()
