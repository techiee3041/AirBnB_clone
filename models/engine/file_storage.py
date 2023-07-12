#!/usr/bin/python3
"""
    Has module containing FileStorage class.
"""

import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}

class FileStorage:
    """
    A class for serializing instances to a
    JSON file and deserializing JSON file to instances.
    """

    # Indicate the json file path
    __file_path = "file.json"

    # dictionary that will store all abjects
    __objects = {}

    def all(sel):
        """Returns the dictionary of all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the object in the dictionary with the key <obj class name>.id.

        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        object_dict = {}

        for key in self.__objects:
            object_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(object_dict, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as json_file:
                n = json.load(json_file)
            for key in n:
                self.__objects[key] = classes[n[key]["__class__"]](**n[key])
        except FileNotFoundError:
            pass
