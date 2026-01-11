#!/usr/bin/python3
"""
Unit tests for City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""
    
    def test_city_inherits_from_base_model(self):
        """Test that City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
    
    def test_city_has_state_id_attribute(self):
        """Test City has state_id attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")
    
    def test_city_has_name_attribute(self):
        """Test City has name attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")
    
    def test_city_attributes_are_strings(self):
        """Test that City attributes are strings"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
    
    def test_city_to_dict(self):
        """Test City to_dict method"""
        city = City()
        city.state_id = "12345"
        city.name = "San Francisco"
        
        city_dict = city.to_dict()
        
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "12345")
        self.assertEqual(city_dict['name'], "San Francisco")


if __name__ == '__main__':
    unittest.main()
