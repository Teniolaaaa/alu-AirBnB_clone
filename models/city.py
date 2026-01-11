#!/usr/bin/python3
"""
City module for AirBnB clone project.
Defines the City class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): The State.id
        name (str): Name of the city
    """

    state_id = ""
    name = ""
