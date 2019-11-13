#!/usr/bin/python3
""" Module for City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class definition """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ ctor of City class """
        super().__init__(**kwargs)
