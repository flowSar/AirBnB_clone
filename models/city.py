#!/usr/bin/python3
"""city model has a Review class that inherent from BaseMode"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Review City inherent from BaseModel and has his own three attribute
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
