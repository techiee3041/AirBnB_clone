#!/usr/bin/python
"""Module with class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inheriting from BaseModel """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
