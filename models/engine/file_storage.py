#!/usr/bin/python3
"""This! module stores instances from the Baseclass"""

import json


class FileStorage:
    """the class for storing instances from the Baseclass
    """
    __file_path = 'file.json'
    __objects ={}

    def all(self):
        return self.__objects

    def new(self, obj):
        key ="{}.{}".format(obj.__class__.name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_obj  ects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
