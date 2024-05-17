#!/usr/bin/python3
"""place model has a Review class that inherent from BaseMode"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Class inherent from BaseModel and has his own attributes
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
