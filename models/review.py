#!/usr/bin/python3
"""review model has a Review class that inherent from BaseMode"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class inherent from BaseModel and has his own three attribute
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method used to initialize class attribute"""
        super().__init__(*args, **kwargs)
