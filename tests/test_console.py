#!/usr/bin/python3
"""
Unit tests for console.py
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


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

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands", output)


if __name__ == '__main__':
    unittest.main()
