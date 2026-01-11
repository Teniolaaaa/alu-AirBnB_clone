#!/usr/bin/python3
"""
Unit tests for Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""
    
    def test_amenity_inherits_from_base_model(self):
        """Test that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
    
    def test_amenity_has_name_attribute(self):
        """Test Amenity has name attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")
    
    def test_amenity_name_is_string(self):
        """Test that Amenity name is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
    
    def test_amenity_to_dict(self):
        """Test Amenity to_dict method"""
        amenity = Amenity()
        amenity.name = "WiFi"
        
        amenity_dict = amenity.to_dict()
        
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "WiFi")


if __name__ == '__main__':
    unittest.main()
