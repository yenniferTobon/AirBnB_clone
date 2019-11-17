#!/usr/bin/python3
"""
Module for FileStorage class and its functions
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from os.path import exists
import json


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}
    __names = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
            "Place": Place
        }

    def all(self):
        """ Returns a dictionary with all objects stored """
        return self.__objects

    def new(self, obj):
        """" Adds a new object to the dictionary objects """
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        """ Saves all the dictionary objects to a json file """
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w+') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """Read the json file and converts the content in objects """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                content = f.read()
                if len(content):
                    new_dict = json.loads(content)
                    for key, value in new_dict.items():
                        cls = key.split(".")
                        self.__objects[key] = self.__names[cls[0]](**value)
