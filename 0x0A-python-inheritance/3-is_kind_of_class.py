#!/usr/bin/python3
"""isinstance checker."""
def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or a subclass of it."""
    return isinstance(obj, a_class)
