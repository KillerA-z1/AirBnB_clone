#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes and deserializes instances to a JSON file."""

    __file_path = "file.json"
    __objects = {}
    __classes = {"BaseModel": BaseModel}

    def all(self, cls=None):
        """Returns the dictionary __objects filtered by class."""
        if cls:
            cls = self.__classes.get(cls)  # Convert class name to class
            if cls is None:
                return {}
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj_class = self.__classes.get(class_name)
                    if obj_class is not None:
                        obj_instance = obj_class(**value)
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Deletes obj from __objects if it’s inside."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def update(self, obj, attr_name, attr_value):
        """Updates an attribute of obj."""
        setattr(obj, attr_name, attr_value)
        self.save()

    def classes(self):
        """Returns a list of class names."""
        return list(self.__classes.keys())

    def __init__(self):
        self.__classes = {
            'BaseModel': BaseModel,
            'User': User,
        }
