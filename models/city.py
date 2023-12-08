#!/usr/bin/python3
""" Defines a City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
      """ Represents a user's city."""
      state_id = ""  # should be State.id
      name = ""