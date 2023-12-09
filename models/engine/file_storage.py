#!/usr/bin/python3
"""This! module stores instances from the Baseclass"""

from datetime import datetime
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """the class for storing instances from the Baseclass
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dict. __objects.
        """
        return self.__objects

    def new(self, obj):
        """ Sets the `obj` with the `key` in `__objects`.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes `__objects` to the JSON file
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ If the JSON file exists, deserializes the file to `__objects`
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():

                    # Remove from the dictionary
                    del value["__class__"]

                    # Ensure conversion to datetime object
                    form = "%Y-%m-%dT%H:%M:%S.%f"
                    ck = "updated_at"  # Attribute to match
                    if ck in value:
                        value[ck] = datetime.strptime(value[ck], form)

                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
