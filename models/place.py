#!/usr/bin/python3
"""
Place module for AirBnB clone project.
Defines the Place class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    
    Attributes:
        city_id (str): The City.id
        user_id (str): The User.id
        name (str): Name of the place
        description (str): Description of the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price per night
        latitude (float): Latitude coordinate
        longitude (float): Longitude coordinate
        amenity_ids (list): List of Amenity.id
    """
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
