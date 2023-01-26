#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """Initializes the square with an optional size"""
        self.size = size

        @property
        def size(self):
            """Getter for the size attribute"""
            return self.__size

        @size.setter
        def size(self, value):
            """Setter for the size attribute"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Returns the current square area"""
                return (self.__size ** 2)
