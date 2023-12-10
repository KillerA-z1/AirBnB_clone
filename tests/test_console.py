#!/usr/bin/python3
"""Module for TestConsole class."""

import unittest
import uuid
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test case class for testing the HBNBCommand class.
    """

    def setUp(self):
        self.console = HBNBCommand()

    def test_prompt(self):
        """Test the prompt attribute of the console."""
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_emptyline(self):
        """Test the behavior of the console when an empty line is entered."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('\n')
            self.assertEqual(fake_out.getvalue(), '')

    def tearDown(self):
        """Clean up after each test."""
        pass

    def test_quit(self):
        """Test the behavior of the console when 'quit' command is entered."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd('quit'))
            self.assertEqual(fake_out.getvalue(), '')

    def test_EOF(self):
        """Test the behavior of the console when 'EOF' command is entered."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd('EOF'))
            self.assertEqual(fake_out.getvalue(), '\n')

    def test_create(self):
        """Test the 'create' command of the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()

            # Check if the output is a valid UUID
            self.assertTrue(uuid.UUID(output))

    def test_show(self):
        """Test the 'show' command of the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('show BaseModel 123')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test the 'all' command of the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('all')
            output = fake_out.getvalue().strip()
            self.assertTrue(output.startswith("["))

    def test_update(self):
        """Test the 'update' command of the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel 123 name "John Doe"')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test the 'destroy' command of the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy BaseModel 123')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
