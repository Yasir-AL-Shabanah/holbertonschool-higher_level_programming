#!/usr/bin/python3
"""Say my name: prints 'My name is <first> <last>'."""


def say_my_name(first_name, last_name=""):
    """Print formatted name with a trailing space if last_name is empty.

    Examples:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Bob")
    My name is Bob 
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
