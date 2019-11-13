#!/usr/bin/python3
"""Module for class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Ctor of State """
        super().__init__(**kwargs)
