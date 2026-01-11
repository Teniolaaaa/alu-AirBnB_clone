#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.
Defines the BaseModel class which will be the parent class for all other models.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    
    Attributes:
        id (str): Unique identifier for each instance
        created_at (datetime): Timestamp when instance is created
        updated_at (datetime): Timestamp when instance is last updated
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        
        Args:
            *args: Variable length argument list (not used)
            **kwargs: Arbitrary keyword arguments for creating instance from dictionary
        """
        from models import storage
        
        if kwargs:
            # Create instance from dictionary representation
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    # Convert string to datetime object
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            # Create new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    def __str__(self):
        """
        Return string representation of the BaseModel instance.
        
        Returns:
            str: String in format [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
    
    def save(self):
        """
        Update the public instance attribute updated_at with current datetime.
        Also saves the instance to the storage.
        """
        from models import storage
        
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        
        Returns:
            dict: Dictionary representation of the instance with:
                - All instance attributes
                - __class__ key with the class name
                - created_at and updated_at in ISO format string
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
