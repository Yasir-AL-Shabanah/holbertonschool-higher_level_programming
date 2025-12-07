#!/usr/bin/python3
"""Module that defines Square with an area() method."""

class Square:
    """Square with validated size and area computation."""

    def __init__(self, size=0):
        """Initialize a Square with validation of size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
