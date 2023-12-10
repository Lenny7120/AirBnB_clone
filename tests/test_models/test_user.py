#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

   # def test_8_attributes(self):
    #    """Tests the attributes of User class."""
     #   attributes_keys = User().__dict__.keys()
      #  o = User()
       # for k in attributes_keys:
        #    print(f"checking attribute: {k}")
         #   self.assertTrue(hasattr(o, k))
          #  if k == ['created_at', 'updated_at']:
           #     expected_type = datetime
            #elif k == 'id':
             #   expected_type = str

            
          #  actual_type = type(getattr(o, k, None))
           # print(actual_type)
            #self.assertEqual(actual_type, expected_type, f"Attribute {k} has unexpected type, got {actual_type} expected {expected_type}")


if __name__ == "__main__":
    unittest.main()
