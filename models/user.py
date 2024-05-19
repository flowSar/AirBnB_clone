#!/usr/bin/python3
"""user model has one class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User Is class that user to create User object and he
        iherent all his functionality from BaseModel
        and he has four public attribute
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init method first"""
        super().__init__(*args, **kwargs)
