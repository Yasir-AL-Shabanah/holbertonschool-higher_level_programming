#!/usr/bin/python3
"""Module that defines Square with input validation on size."""

class Square:
    """Square validating that size is an int >= 0."""

    def __init__(self, size=0):
        """Initialize a Square, validating type and value."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
