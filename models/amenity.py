#!/usr/bin/python3
"""amenity model has a Review class that inherent from BaseMode"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class inherent from BaseModel and has his own attributes
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method used to initialize instance attribute"""
        super().__init__(*args, **kwargs)
