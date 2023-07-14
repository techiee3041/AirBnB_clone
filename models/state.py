#!/usr/bin/python3
"""Model containing state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class inheriting from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the state instance"""
        super().__init__(*args, **kwargs)
