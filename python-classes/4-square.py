#!/usr/bin/python3
"""Module 4-square: expose size via @property with validation."""
class Square:
    """Square exposing a size property with checks."""
    def __init__(self, size=0):
        """Init with validation (int >= 0)."""
        self.size = size

    @property
    def size(self):
        """Getter: return current side length (int)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: validate and set side length.

        Raises:
            TypeError: if value is not int.
            ValueError: if value < 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area (size*size)."""
        return self.__size * self.__size
