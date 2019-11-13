#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Ctor for Amenity class """
        super().__init__(**kwargs)
