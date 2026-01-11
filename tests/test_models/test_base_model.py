#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test fixtures"""
        pass

    def tearDown(self):
        """Tear down test fixtures"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test creating a new instance of BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_is_string(self):
        """Test that id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_ids(self):
        """Test that each instance has a unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        """Test string representation of BaseModel"""
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)

    def test_save_method(self):
        """Test save method updates updated_at"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method returns correct dictionary"""
        model = BaseModel()
        model.name = "Test Model"
        model.number = 123
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['number'], 123)

    def test_to_dict_datetime_format(self):
        """Test that datetime objects are in ISO format in to_dict"""
        model = BaseModel()
        model_dict = model.to_dict()

        created_at = datetime.strptime(model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(model_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_create_from_dict(self):
        """Test creating an instance from dictionary"""
        model1 = BaseModel()
        model1.name = "Test Model"
        model1.number = 123
        model1_dict = model1.to_dict()

        model2 = BaseModel(**model1_dict)

        self.assertEqual(model1.id, model2.id)
        self.assertEqual(model1.created_at, model2.created_at)
        self.assertEqual(model1.updated_at, model2.updated_at)
        self.assertEqual(model1.name, model2.name)
        self.assertEqual(model1.number, model2.number)
        self.assertIsNot(model1, model2)

    def test_create_from_dict_with_class(self):
        """Test that __class__ is not added as attribute"""
        model1 = BaseModel()
        model1_dict = model1.to_dict()
        model2 = BaseModel(**model1_dict)

        self.assertNotIn('__class__', model2.__dict__)


if __name__ == '__main__':
    unittest.main()
