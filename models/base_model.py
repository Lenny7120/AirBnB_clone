#!/usr/bin/python3
""" Defines common attributes & methods for other classes.
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Represents a backbone for all other classes.
        Defines the common attributes & methods.
    """

    def __init__(self, *args, **kwargs):
        """ Initialized a new BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    self.id = str(uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a printable representation of the obj.
        """
        return "[self.__class__.__name__] (self.id) self.__dict__"

    def save(self):
        """ Updates the `updated_at` to current date-time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dic. containing all keys/values of
            `__dict__` of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
