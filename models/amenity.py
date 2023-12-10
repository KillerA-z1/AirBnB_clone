#!/usr/bin/python3
"""This module creates a Amenity class  that inherits from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects"""

    name = ""
