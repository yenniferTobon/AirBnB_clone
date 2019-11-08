#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) is not 0:
            self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.id = kwargs["id"]
        else:
            self.updated_at = datetime.today()
            self.created_at = datetime.today()
            self.id = str(uuid4())

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
     
            
