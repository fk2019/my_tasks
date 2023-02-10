#!/usr/bin/env python3
"""
Moduel Serializes and deserializes JSON
"""

import json
import os

class FileStorage():
    """This class serializes instances to JSON and vice versa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects, the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj.to_dict()

    def save(self):
        """Serializes __objects to JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="a+", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    data[key] = self.__objects
                f.seek(0)
                json.dump(data, f)
                #f.write(json.dumps(self.__objects))
        else:
            with open(self.__file_path, mode="w", encoding="utf-8") as f:
                f.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.load(f)
                for key in self.__objects.items():
                    self.__objects[key] = data
