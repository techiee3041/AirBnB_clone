#!/usr/bin/python3

"""Model containing City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City instance"""
        super().__init__(*args, **kwargs)
