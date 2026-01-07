#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Subclass of list that prints a sorted list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
