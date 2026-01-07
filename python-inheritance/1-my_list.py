#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """A custom list with a method to print it sorted."""

    def print_sorted(self):
        """Print the list in ascending order (does not modify the original)."""
        print(sorted(self))
