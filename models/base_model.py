#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Defines the base model for other classes."""
    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Keyword arguments used to initialize attributes.
                      If present, sets attributes based on key-value pairs.
                      Converts 'created_at' & 'updated_at' strings to datetime.
                      If absent, generates new id, created_at, and updated_at
                      values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date_format = '%Y-%m-%dT%H:%M:%S.%f'
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A formatted string containing the class name, id,
            and attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing the attributes of the BaseModel.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
