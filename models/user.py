#!/usr/bin/python3
"""Defines a User."""

from models.base_model import BaseModel


class User(BaseModel):
      """ A user."""
      email = ""
      password = ""
      first_name = ""
      last_name = ""