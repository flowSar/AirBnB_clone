#!/usr/bin/python3
"""
    base_model is python module where we define a BaseModel class
"""
import uuid
from datetime import datetime, date


class BaseModel:
    """
        __init__ method for initialize the object state when it created_at
        in this case we initialize our object with id, create_at,
        and updated_at
    """
    def __init__(self, *args, **kwargs):
        if (len(kwargs) != 0):
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """__str__ method return a respresentation of an object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        """ to_dict return a dictionary that represention all object
            attribute and name
        """
        my_dict = self.__dict__
        MCS = microseconds
        date_time_obj = my_dict["created_at"].isoformat(timespec='MCS')
        my_dict["created_at"] = date_time_obj
        date_time_obj = my_dict["updated_at"].isoformat(timespec='MCS')
        my_dict["updated_at"] = date_time_obj
        dict_class = {"__class__": self.__class__.__name__}
        dict_class.update(my_dict)

        return dict_class
