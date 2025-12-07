#!/usr/bin/python3
"""Module 6-square: add position offset to printing and to __str__."""
class Square:
    """Square with size and position controlling visual offset."""
    def __init__(self, size=0, position=(0, 0)):
        """Init with validation for size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter: current side length."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: size must be int >= 0."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter: tuple (x_offset, y_offset), both >= 0."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter: validate a 2-int tuple with non-negative values."""
        if (type(value) is not tuple or len(value) != 2 or
            type(value[0]) is not int or type(value[1]) is not int or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print with vertical/top and horizontal/left offsets."""
        if self.__size == 0:
            print("")
            return
        # vertical offset
        for _ in range(self.__position[1]):
            print("")
        # content with horizontal offset
        pad = " " * self.__position[0]
        for _ in range(self.__size):
            print(pad + ("#" * self.__size))

    def __str__(self):
        """Return the printable string (used by print())."""
        if self.__size == 0:
            return ""
        lines = []
        lines.extend([""] * self.__position[1])
        pad = " " * self.__position[0]
        for _ in range(self.__size):
            lines.append(pad + ("#" * self.__size))
        return "\n".join(lines)
