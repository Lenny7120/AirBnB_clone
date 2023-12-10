#!/usr/bin/python3

"""Unittest module for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_FileStorage_initialize(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_instantiate_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiate_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    pass


class TestFileStorage_methods(unittest.TestCase):
    """Test cases for methods in the FileStorage class."""

    def setUp(self):
        try:
            os.rename("file.json", "temp_file")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp_file", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        #  instantiate
        amenity = Amenity()
        base = BaseModel()
        city = City()
        place = Place()
        review = Review()
        state = State()
        user = User()

        # store to file
        models.storage.new(amenity)
        models.storage.new(base)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(review)
        models.storage.new(state)
        models.storage.new(user)

        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_save(self):
        text = ""

        #  instantiate
        amenity = Amenity()
        base = BaseModel()
        city = City()
        place = Place()
        review = Review()
        state = State()
        user = User()

        # store to file
        models.storage.new(amenity)
        models.storage.new(base)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(review)
        models.storage.new(state)
        models.storage.new(user)
        models.storage.save()

        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("Amenity." + amenity.id, text)
            self.assertIn("BaseModel." + base.id, text)
            self.assertIn("City." + city.id, text)
            self.assertIn("Place." + place.id, text)
            self.assertIn("Review." + review.id, text)
            self.assertIn("State." + state.id, text)
            self.assertIn("User." + user.id, text)

    def test_reload(self):
        #  instantiate
        amenity = Amenity()
        base = BaseModel()
        city = City()
        place = Place()
        review = Review()
        state = State()
        user = User()

        # store to file
        models.storage.new(amenity)
        models.storage.new(base)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(review)
        models.storage.new(state)
        models.storage.new(user)
        models.storage.save()
        models.storage.reload()

        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, obj)
        self.assertIn("User." + user.id, obj)
        self.assertIn("State." + state.id, obj)
        self.assertIn("Place." + place.id, obj)
        self.assertIn("City." + city.id, obj)
        self.assertIn("Amenity." + amenity.id, obj)
        self.assertIn("Review." + review.id, obj)


if __name__ == "__main__":
    unittest.main()
