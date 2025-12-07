#!/usr/bin/python3
"""Module that defines Square with size and position offsets for printing."""

class Square:
    """Square that supports horizontal/vertical offsets via position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current (x, y) print offset."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position as a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square considering the position offsets."""
        if self.__size == 0:
            print("")
            return
        # vertical offset
        print("\n" * self.__position[1], end="")
        # each row: left padding + hashes
        for _ in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))
