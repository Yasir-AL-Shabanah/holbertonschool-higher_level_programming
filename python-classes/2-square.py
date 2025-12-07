#!/usr/bin/python3
"""Module 2-square: validate size type/value at construction."""
class Square:
    """Square that validates size is an int >= 0."""
    def __init__(self, size=0):
        """Init with validation.

        Args:
            size: length of a side (int >= 0).

        Raises:
            TypeError: if size is not an int.
            ValueError: if size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
