#!/usr/bin/python3
"""
Review module for AirBnB clone project.
Defines the Review class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The Place.id
        user_id (str): The User.id
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
