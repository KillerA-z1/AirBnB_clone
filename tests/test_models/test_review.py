#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test case class for testing the Review class.
    """

    def setUp(self):
        self.review = Review()

    def test_place_id(self):
        """Test the place_id attribute of the Review class."""
        self.assertEqual("", self.review.place_id)

    def test_user_id(self):
        """Test the user_id attribute of the Review class."""
        self.assertEqual("", self.review.user_id)

    def test_text(self):
        """Test the text attribute of the Review class."""
        self.assertEqual("", self.review.text)

    def tearDown(self):
        """Clean up after each test."""
        pass


if __name__ == '__main__':
    unittest.main()
