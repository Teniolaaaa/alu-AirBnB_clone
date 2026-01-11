#!/usr/bin/python3
"""
Unit tests for User class.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""
    
    def test_user_inherits_from_base_model(self):
        """Test that User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
    
    def test_user_has_email_attribute(self):
        """Test User has email attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")
    
    def test_user_has_password_attribute(self):
        """Test User has password attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")
    
    def test_user_has_first_name_attribute(self):
        """Test User has first_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")
    
    def test_user_has_last_name_attribute(self):
        """Test User has last_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")
    
    def test_user_attributes_are_strings(self):
        """Test that User attributes are strings"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
    
    def test_user_to_dict(self):
        """Test User to_dict method"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        
        user_dict = user.to_dict()
        
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")


if __name__ == '__main__':
    unittest.main()
