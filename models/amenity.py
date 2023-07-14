#!/usr/bin/python3
"""Module with amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity inheriting from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity class"""
        super().__init__(*args, **kwargs)
