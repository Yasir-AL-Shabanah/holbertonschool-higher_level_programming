#!/usr/bin/python3
"""Module 3-square: compute the area of a validated square."""
class Square:
    """Square with area()."""
    def __init__(self, size=0):
        """Init with validation (int >= 0)."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area (size*size)."""
        return self.__size * self.__size
