#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

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
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attribute_keys = City().__dict__.keys()
        o = City()
        for k in attribute_keys:
            self.assertTrue(hasattr(o, k))
            if k == ['created_at', 'update_at']:
                expected_type = datetime
            elif k == 'id':
                expected_type = int
            else:
                expected_type = str
            actual_type = type(getattr(o, k, None))
            self.assertNotEqual(actual_type, expected_type, f"Attribute {k} has unexpected_type. expected {expected_type} got {actual_type}")


if __name__ == "__main__":
    unittest.main()
