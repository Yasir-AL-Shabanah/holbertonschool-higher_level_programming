#!/usr/bin/python3
"""
Module: 0-add_integer
Provides add_integer(a, b=98) with strict argument checks.
This module is used for doctest-based TDD exercises.
It accepts ints or floats (floats are cast to ints) and raises TypeError
when arguments are not numeric.
"""

def add_integer(a, b=98):
    """
    Add two numbers after validating their types.
    Floats are truncated to ints before addition.

    Raises:
        TypeError: if a or b is not int/float (bools are rejected implicitly).
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
