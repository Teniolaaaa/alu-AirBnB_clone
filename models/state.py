#!/usr/bin/python3
"""
State module for AirBnB clone project.
Defines the State class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Attributes:
        name (str): Name of the state
    """

    name = ""
