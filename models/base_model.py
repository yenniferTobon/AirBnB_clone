#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *argv, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        self.argv = argv
	self.kwargs = kwargs

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = BaseModel.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
     
            
