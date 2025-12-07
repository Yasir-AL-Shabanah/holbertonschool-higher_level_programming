#!/usr/bin/python3
"""Unittests for max_integer(list=[])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_beginning(self):
        self.assertEqual(max_integer([9, 1, 3, 2]), 9)

    def test_single(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negatives(self):
        self.assertEqual(max_integer([-5, -3, -9, -4]), -3)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 2]), 3)


if __name__ == "__main__":
    unittest.main()
