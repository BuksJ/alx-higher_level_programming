#!/usr/bin/python3
"""defines a square by private instance attribute size"""


class Square:
    def __init__(self, size=0):
        """Initialize the square class with size attribute."""
        self.size = size

        @property
        def size(self):
            """Retrieve the size of the square"""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of the square"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Returns the current square area"""
                return (self.__size ** 2)
