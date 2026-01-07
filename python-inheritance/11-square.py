#!/usr/bin/python3
"""Define Square with size property."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize square."""
        super().__init__(size, size)

    def __str__(self):
        """Return string representation."""
        return "[Square] {}/{}".format(self.size, self.size)

    @property
    def size(self):
        """Get size."""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Set size after validation."""
        self.integer_validator("size", value)
        self._Rectangle__width = value
        self._Rectangle__height = value
