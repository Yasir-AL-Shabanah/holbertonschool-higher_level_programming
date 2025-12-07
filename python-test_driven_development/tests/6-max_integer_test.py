#!/usr/bin/python3
"""Unittests for the provided max_integer function."""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 2, 7, 1]), 7)

    def test_negative(self):
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([9]), 9)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.5, 3.4]), 3.5)

    def test_mixed(self):
        self.assertEqual(max_integer([1, 2.2, 2]), 2.2)

if __name__ == "__main__":
    unittest.main()
