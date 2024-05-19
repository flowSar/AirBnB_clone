#!/usr/bin/python3
"""test_base_models is dedicate to test base_model module
    and his has one unittst class and many function for testing
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime as dtime


class TestBaseModel(unittest.TestCase):

    def test_to_dict(self):
        dict_test = {"__class__": "BaseModel",
                     "id": "709cb71f-fd9f-4b1e-a2a9-c042f25e2c18",
                     "created_at": "2024-05-18T23:23:31.377466",
                     "updated_at": "2024-05-18T23:23:31.377730",
                     "email": "email@gmail.com"}

        base = BaseModel(**dict_test)
        self.assertEqual(base.to_dict(), dict_test)

    def test_init(self):
        dict_test = {"__class__": "BaseModel",
                     "id": "709cb71f-fd9f-4b1e-a2a9-c042f25e2c18",
                     "created_at": "2024-05-18T23:23:31.377466",
                     "updated_at": "2024-05-18T23:23:31.377730",
                     "email": "email@gmail.com"}

        base = BaseModel(**dict_test)
        self.assertEqual("2024-05-18T23:23:31.377466",
                         f"{dtime.isoformat(base.__dict__['created_at'])}")
        self.assertEqual("2024-05-18T23:23:31.377730",
                         f"{dtime.isoformat(base.__dict__['updated_at'])}")
        self.assertEqual("709cb71f-fd9f-4b1e-a2a9-c042f25e2c18",
                         base.__dict__['id'])
        self.assertNotEqual(f"{dtime.isoformat(base.__dict__['created_at'])}",
                            f"{dtime.isoformat(base.__dict__['updated_at'])}")


if __name__ == '__main__':
    unittest.main()
