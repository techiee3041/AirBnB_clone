#!/usr/bin/python3
"""
    Module which has Basemodel class
"""

import uuid
from datetime import datetime as dt
import time

t = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        Base class for all models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.


        Args:
            *args: Variable length of arguments(unused)

            **kwargs: Dictionary containing keys and values representing
            created_at and updated_at. Th values should be in string in the
            format %Y-%m-%dT%H:%M:%S.%f.

        """
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = dt.strptime(kwargs["created_at"], t)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = dt.strptime(kwargs["updated_at"], t)

    def __str__(self):
        """
            Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        this_dict = self.__dict__.copy()
        this_dict["created_at"] = self.created_at.isoformat()
        this_dict["updated_at"] = self.updated_at.isoformat()
        this_dict["__class__"] = self.__class__.__name__
        return this_dict
