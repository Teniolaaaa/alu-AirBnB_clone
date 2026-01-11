#!/usr/bin/python3
"""
Unit tests for console.py
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Set up test fixtures"""
        pass

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("")
            self.assertIsNone(result)
            self.assertEqual(f.getvalue(), "")

    def test_emptyline_with_spaces(self):
        """Test empty line with spaces"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("   ")
            self.assertIsNone(result)
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
