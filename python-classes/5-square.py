#!/usr/bin/python3
"""Module that defines Square with printable representation."""

class Square:
    """Square that can print itself with '#' characters."""

    def __init__(self, size=0):
        """Initialize a Square using size property."""
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

    def my_print(self):
        """Print the square using '#' or print a blank line if size is 0."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
