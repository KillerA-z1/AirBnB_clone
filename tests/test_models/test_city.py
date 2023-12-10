#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test case class for testing the City class.
    """

    def test_attributes(self):
        """Test the attributes of the City class."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
