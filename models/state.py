#!/usr/bin/python3
"""state model has one class named State"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class has one pulic attribute
        name: is public attribute
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method used to initialize class attribute"""
        super().__init__(*args, **kwargs)
