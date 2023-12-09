#!/usr/bin/python3
""" Defines a Place class."""


from models.base_model import BaseModel


class Place(BaseModel):

    """ Represents a place."""

    city_id = ""  # it will be City.id
    user_id = ""  # it will be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id
