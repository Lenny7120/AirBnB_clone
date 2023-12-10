#!/usr/bin/python3

"""Unittest module for FileStorage class."""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime

class TestFileStorage(unittest.TestCase):
    pass