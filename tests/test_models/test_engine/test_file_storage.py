#!/usr/bin/python3
"""Module for TestFileStorage class."""

import unittest
import json
import tempfile
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class to test the FileStorage class."""

    def setUp(self):
        """Set up method to create an instance of FileStorage."""
        self.storage = FileStorage()

    def test_all(self):
        """Test if all() returns the correct dictionary."""
        # Create an instance of BaseModel for testing
        obj = BaseModel()
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)

        # Check if the dictionary contains the expected key
        self.assertIn(key, self.storage.all())

    def test_new(self):
        """Test if new() adds the object to __objects dictionary."""
        obj = BaseModel()
        self.storage.new(obj)
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test if save() serializes __objects to the JSON file."""
        obj = BaseModel()
        self.storage.new(obj)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_filename = temp_file.name

        self.storage._FileStorage__file_path = temp_filename
        self.storage.save()

        # Check if the file exists and contains the serialized object
        with open(temp_filename, 'r') as file:
            data = json.load(file)
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.assertIn(key, data)

    def test_reload(self):
        """Test if reload() deserializes the JSON file to __objects."""
        obj = BaseModel()
        self.storage.new(obj)

        with tempfile.NamedTemporaryFile(mode='w') as temp_file:
            temp_filename = temp_file.name
            self.storage._FileStorage__file_path = temp_filename
            self.storage.save()

            # Clear __objects and reload from the temporary file
            self.storage._FileStorage__objects = {}
            self.storage.reload()

        # Check if the object is loaded back into __objects
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def tearDown(self):
        """Clean up any temporary files after each test."""
        pass


if __name__ == '__main__':
    unittest.main()
