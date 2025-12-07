#!/usr/bin/python3
"""Module 5-square: add printable representation using '#'. """
class Square:
    """Square with area() and my_print()."""
    def __init__(self, size=0):
        """Init with validation (int >= 0)."""
        self.size = size

    @property
    def size(self):
        """Getter: current side length."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: validate length then store it."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#'; print empty line if size == 0."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
