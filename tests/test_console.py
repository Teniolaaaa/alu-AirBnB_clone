#!/usr/bin/python3
"""
Unit tests for console.py
"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Set up test fixtures"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

    def test_create_base_model(self):
        """Test create BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show_missing_class(self):
        """Test show with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

    def test_show_invalid_class(self):
        """Test show with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

    def test_show_no_instance_found(self):
        """Test show with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

    def test_destroy_missing_class(self):
        """Test destroy with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

    def test_destroy_no_instance_found(self):
        """Test destroy with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertTrue(isinstance(f.getvalue().strip(), str))

    def test_all_invalid_class(self):
        """Test all with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

    def test_update_missing_class(self):
        """Test update with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

    def test_update_invalid_class(self):
        """Test update with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

    def test_update_no_instance_found(self):
        """Test update with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertTrue(output.isdigit())

    def test_all_dot_notation(self):
        """Test Class.all() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            self.assertTrue("[" in f.getvalue())

    def test_show_dot_notation(self):
        """Test Class.show() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User')
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.show("{user_id}")')
            self.assertTrue(user_id in f.getvalue())

    def test_destroy_dot_notation(self):
        """Test Class.destroy() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User')
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.destroy("{user_id}")')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.show("{user_id}")')
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

    def test_update_dot_notation(self):
        """Test Class.update() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User')
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                f'User.update("{user_id}", "first_name", "John")')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.show("{user_id}")')
            self.assertTrue("John" in f.getvalue())


if __name__ == '__main__':
    unittest.main()
