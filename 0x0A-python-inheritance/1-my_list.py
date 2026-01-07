#!/usr/bin/python3
"""Defines class MyList that inherits from list."""
class MyList(list):
    """Custom list class with print_sorted() method."""
    def print_sorted(self):
        """Print list elements in ascending order."""
        print(sorted(self))
