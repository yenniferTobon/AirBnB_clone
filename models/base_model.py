#!/usr/bin/python3
"""
Module for class BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """ BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """ Ctor of BaseModel class """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.today()
            self.created_at = datetime.today()
            self.id = str(uuid4())
            models.storage.new(self)                

    def __str__(self):
        """ prints the representation string of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Saves the instance to a json file"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of the instance """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
