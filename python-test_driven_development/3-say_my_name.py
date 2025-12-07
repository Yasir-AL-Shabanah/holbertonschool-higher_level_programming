#!/usr/bin/python3
"""
Say a full name with exact spacing requirements.
"""


def say_my_name(first_name, last_name=""):
    """Print: My name is <first_name> <last_name> (trailing space allowed)."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Always keep the single space between names, even if last_name == ""
    print("My name is {} {}".format(first_name, last_name))
