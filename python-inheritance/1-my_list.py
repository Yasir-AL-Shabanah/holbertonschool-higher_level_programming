#!/usr/bin/python3
"""Define MyList that inherits from list."""


class MyList(list):
    """Custom list with print_sorted()."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
