#!/usr/bin/python3
"""Module that defines Square using @property for managed size."""

class Square:
    """Square exposing a size property with validation."""

    def __init__(self, size=0):
        """Initialize a Square using the property setter."""
        self.size = size

    @property
    def size(self):
        """Get the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
