#!/usr/bin/python3
"""Function that checks exact class type."""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class.
    Otherwise return False.
    """
    return type(obj) is a_class
