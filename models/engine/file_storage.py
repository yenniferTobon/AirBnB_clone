#!/usr/bin/python3

from os.path import exists
import json

class FileStorage:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] =  obj.to_dict()
        with open(self.__file_path, 'w+') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                content = f.read()
                if len(content):
                    self.__objects = json.loads(f.read())
