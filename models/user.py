#!/usr/bin/python3
"""
Module for User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
