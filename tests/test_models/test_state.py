#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_state(self):
        """Test for the State class."""
        state = State()
        self.assertEqual(state.name, "")
        state.name = "California"
        self.assertEqual(state.name, "California")
        self.assertEqual(state.to_dict()["name"], "California")


if __name__ == '__main__':
    unittest.main()
