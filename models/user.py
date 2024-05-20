#!/usr/bin/python3
"""user model has one class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Is subclass of BaseModel and he 
        iherent all his functionality from BaseModel
        and he has four public attribute
    """
    email = None
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init method for initilizing class attribute"""
        super().__init__(*args, **kwargs)
        User.email = ""
