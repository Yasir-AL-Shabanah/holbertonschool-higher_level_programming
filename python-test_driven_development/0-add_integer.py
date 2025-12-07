#!/usr/bin/python3
"""
Module: 0-add_integer
Provides add_integer(a, b=98) with strict argument checks.
"""

def add_integer(a, b=98):
    """
    Add two numbers after validating their types.
    Floats are truncated to ints before addition.

    Raises:
        TypeError: if a or b is not int/float (bools rejected).
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
