#!/usr/bin/python3
"""Function that checks class or inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class
    or of a class that inherited from a_class.
    Otherwise return False.
    """
    return isinstance(obj, a_class)
