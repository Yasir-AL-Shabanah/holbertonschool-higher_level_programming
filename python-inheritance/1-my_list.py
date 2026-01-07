#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list with a method to print a sorted version."""

    def print_sorted(self):
        """
        Print the list in ascending order
        without modifying the original list.
        """
        print(sorted(self))
