#!/usr/bin/python3
"""Unit tests for max_integer(list=[]) using unittest."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_begin(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_single(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negatives(self):
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_floats(self):
        self.assertAlmostEqual(max_integer([1.5, 2.7, 2.6]), 2.7)


if __name__ == "__main__":
    unittest.main()
