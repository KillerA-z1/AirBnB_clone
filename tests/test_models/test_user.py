#!/usr/bin/python3
"""Unittest Module for TestUser class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test case for the User class.
    """

    def test_attributes(self):
        """Test the attributes of the User class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
