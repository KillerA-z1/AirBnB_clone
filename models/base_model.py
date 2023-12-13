#!/usr/bin/python3
""" Defines the BaseModel class."""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines the base model for other classes.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The date and time the instance was created.
        updated_at (datetime): The date and time the instance was last updated.
    """

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
                        # Convert date strings to datetime objects
                        date_format = '%Y-%m-%dT%H:%M:%S.%f'
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            # Generate new id, created_at, and updated_at values
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing the attributes of the BaseModel
                in the desired order.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def save(self):
        """
        Update the public instance attribute updated_at with the current
        datetime and save to the JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()
