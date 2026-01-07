#!/usr/bin/python3
"""Checks if object is instance of a class or inherited from it."""
def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or subclass."""
    return isinstance(obj, a_class)
