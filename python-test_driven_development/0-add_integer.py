#!/usr/bin/python3
"""Add two integers with validation."""

def add_integer(a, b=98):
    """Return int(a) + int(b).
    Raise TypeError if a or b is not int/float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
