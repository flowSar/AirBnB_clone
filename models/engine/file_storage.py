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
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

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
        for key in self.__objects.keys():
            obj = self.__objects[key]
            json_data[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()
 
        with open(self.__file_path, "w") as f:
            json.dump(json_data, f)
        self.__objects = {}
    def reload(self):
        """
            reload: this methode is for loading data from json file to
            generate new objects from each object in jsonfile
        """

        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)

            for key in json_data:
                obj = BaseModel(**(json_data[key]))
                self.__objects[key] = obj
        except FileNotFoundError:
            pass 
