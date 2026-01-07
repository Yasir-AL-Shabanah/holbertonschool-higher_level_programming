#!/usr/bin/python3
"""Strict subclass checker."""
def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass of a_class (not a_class)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
