import json
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    # Add your testing methods here, for example:
    def test_create(self, mock_stdout):
        with patch('builtins.input',
                   return_value="create BaseModel") as mock_input:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn("BaseModel", mock_stdout.getvalue())

    # Add more testing methods based on your console functionality

    def test_base_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        model_str = "[BaseModel] ({}) {}".format(my_model.id,
                                                 my_model.__dict__)
        self.assertEqual(str(my_model), model_str)
        my_model.save()
        self.assertIsNotNone(my_model.updated_at)
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], "BaseModel")
        self.assertEqual(type(my_model_json['created_at']), str)
        self.assertEqual(type(my_model_json['updated_at']), str)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key,
                                           type(my_model_json[key]),
                                           my_model_json[key]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn("BaseModel", mock_stdout.getvalue())

    # Add more testing methods based on your console functionality


if __name__ == '__main__':
    unittest.main()
