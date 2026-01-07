#!/usr/bin/python3
"""Checks if object is instance of a subclass of a_class."""
def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (not same type)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
