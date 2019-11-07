#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        new_dict = {}
        new_dict["__class__"] = BaseModel.__name__
        for key,value in self.__dict__.items():
            v = value
            if key == "created_at" or key == "updated_at":
                v = v.isoformat()
            new_dict[key] = v
        return new_dict

     
            
