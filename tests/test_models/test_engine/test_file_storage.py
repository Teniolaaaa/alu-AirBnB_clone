#!/usr/bin/python3
"""
Unit tests for FileStorage class.
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""
    
    def setUp(self):
        """Set up test fixtures"""
        pass
    
    def tearDown(self):
        """Tear down test fixtures"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test_file_storage_instance(self):
        """Test FileStorage instance creation"""
        self.assertIsInstance(storage, FileStorage)
    
    def test_all_method(self):
        """Test all method returns dictionary"""
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
    
    def test_new_method(self):
        """Test new method adds object to storage"""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())
    
    def test_save_method(self):
        """Test save method writes to file"""
        model = BaseModel()
        model.save()
        self.assertTrue(os.path.exists("file.json"))
    
    def test_reload_method(self):
        """Test reload method loads objects from file"""
        model = BaseModel()
        model.name = "Test Model"
        model.save()
        
        # Clear storage
        storage._FileStorage__objects = {}
        
        # Reload
        storage.reload()
        
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())
        reloaded_model = storage.all()[key]
        self.assertEqual(reloaded_model.name, "Test Model")
    
    def test_save_and_reload_multiple_objects(self):
        """Test saving and reloading multiple objects"""
        model1 = BaseModel()
        model2 = BaseModel()
        user1 = User()
        
        model1.save()
        model2.save()
        user1.save()
        
        # Clear storage
        storage._FileStorage__objects = {}
        
        # Reload
        storage.reload()
        
        key1 = "BaseModel.{}".format(model1.id)
        key2 = "BaseModel.{}".format(model2.id)
        key3 = "User.{}".format(user1.id)
        
        self.assertIn(key1, storage.all())
        self.assertIn(key2, storage.all())
        self.assertIn(key3, storage.all())
    
    def test_reload_nonexistent_file(self):
        """Test reload with nonexistent file doesn't raise error"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        
        # Should not raise exception
        storage.reload()


if __name__ == '__main__':
    unittest.main()
