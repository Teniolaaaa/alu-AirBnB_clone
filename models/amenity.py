#!/usr/bin/python3
"""
Amenity module for AirBnB clone project.
Defines the Amenity class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    
    Attributes:
        name (str): Name of the amenity
    """
    
    name = ""
