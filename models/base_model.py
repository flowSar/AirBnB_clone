#!/usr/bin/python3
"""
    base_model is python module where we define a BaseModel class
    and the class of this module will serve a base class of all
    classes that will create .
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
        __init__ method for initialize the object state when it created_at
        in this case we initialize our object with id, create_at,
        and updated_at
    """

    def __init__(self, *args, **kwargs):
        """init method used to initialize class attribute"""
        if (len(kwargs) != 0):
            for key in kwargs.keys():
                if key == '__class__':
                    pass
                elif key == 'created_at':
                    DateTimeCr = datetime.fromisoformat(kwargs['created_at'])
                    setattr(self, key, DateTimeCr)
                elif key == 'updated_at':
                    DateTimeUp = datetime.fromisoformat(kwargs['updated_at'])
                    setattr(self, key, DateTimeUp)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """__str__ is a magic method return a respresentation of an object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            update instace time and save instance to the json file
            by using storage instance
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
            to_dict return a dictionary that represention all object
            attribute and name in type of dictionary. and update the
            formate of time.
            Return:
                dictionay represent of object_attributes
        """
        my_dict = self.__dict__.copy()
        MCS = 'microseconds'
        date_time_obj1 = my_dict['created_at'].isoformat(timespec=MCS)
        my_dict['created_at'] = date_time_obj1
        date_time_obj2 = my_dict["updated_at"].isoformat(timespec=MCS)
        my_dict['updated_at'] = date_time_obj2
        my_dict['__class__'] = self.__class__.__name__

        return my_dict
