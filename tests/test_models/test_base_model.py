#!/usr/bin/python3
"""Module for TestbaseConsole class."""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """
    Test case class for testing the BaseModel class.
    """

    def setUp(self):
        """ Create a temporary file for testing. """
        self.temp_file_path = "temp_file.json"
        models.storage._FileStorage__file_path = self.temp_file_path
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """ Remove the temporary file after testing. """
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def test_init(self):
        """ Test if the attributes are set correctly during initialization. """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str(self):
        """ Test the __str__ method """
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id,
                                                    my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_to_dict(self):
        """ Test the to_dict method """
        my_model = BaseModel()
        my_model.my_number = 42
        my_model.name = "Test Model"
        my_model_dict = my_model.to_dict()

        # Check if the dictionary has the expected keys and values
        self.assertIn('my_number', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)

        self.assertEqual(my_model_dict['my_number'], 42)
        self.assertEqual(my_model_dict['name'], "Test Model")
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_save(self):
        """ Test the save method """
        my_model = BaseModel()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_model.save()
            self.assertIn("", mock_stdout.getvalue().strip())

    def test_reload(self):
        """ Test the reload method """
        my_model = BaseModel()
        my_model.save()

        # Save the changes to the file before reloading
        models.storage.save()

        # Reload data from the file
        models.storage.reload()

        # Retrieve the saved object
        new_model = models.storage.all()["BaseModel.{}".format(my_model.id)]

        # Check if the new instance has the same attributes as saved instance
        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)


if __name__ == '__main__':
    unittest.main()
