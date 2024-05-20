#!/usr/bin/python3
"""
    file_storage module didicated to store all object data
    to json file
"""
import json
import os


class FileStorage:

    """
        class FileStorage : continue all method needed for storing
        object data to json file , and works by updating json file
        each time we created new object
    """
    __file_path = None
    __objects = {}

    def __init__(self):
        """this function used for initilize class attribute when object
            is created.
        """
        self.__file_path = "file.json"

    def all(self):
        """
            all method return dictionay of all object we created
            Return:
                dictionay of objects
        """
        return self.__objects

    def new(self, obj):
        """
            this methode add new object to self.__objects as key:value
            args:
                obj: new pbject
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
            save:after we load old(fron json file with method reload)
            and new objects to self.__objects.keys
            this method works on saving each of this object
            and its attributes to json file,
        """
        json_data = {}
        self.reload()
        for key in self.__objects.keys():
            obj = self.__objects[key]
            json_data[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(json_data, f)
        json_data = {}

    def reload(self):
        """
            reload: this methode is for loading data from json file to
            generate new objects from each object in jsonfile
        """
        try:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)

            for key in json_data:
                obj_name = key.split(".")[0]
                new_object = self.get_right_object(obj_name, json_data[key])
                if new_object is not None:
                    self.__objects[key] = new_object
        except FileNotFoundError:
            pass

    def get_right_object(self, obj_name, dic):
        """this method for getting the creating the right new object
            and it's attributes based on the giving name and data
            Return:
                new object or null if the name doesn't exist
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity

        object_list = {"BaseModel": BaseModel,
                       "User": User,
                       "State": State,
                       "Review": Review,
                       "Place": Place,
                       "City": City
                       }
        for key in object_list:
            if (obj_name == key):
                new_object = object_list[key](**dic)
                return new_object
