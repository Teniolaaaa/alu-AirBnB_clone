#!/usr/bin/python3
"""
Unit tests for State class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_state_inherits_from_base_model(self):
        """Test that State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_has_name_attribute(self):
        """Test State has name attribute"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_state_name_is_string(self):
        """Test that State name is a string"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_to_dict(self):
        """Test State to_dict method"""
        state = State()
        state.name = "California"

        state_dict = state.to_dict()

        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "California")


if __name__ == '__main__':
    unittest.main()
