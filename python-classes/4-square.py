#!/usr/bin/python3
class Square:
    """Square with managed size property."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size
