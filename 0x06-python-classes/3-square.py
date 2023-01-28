#!/usr/bin/python3
"""Defines a square by private instance attribute size
and instantiation with optional size"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the square class with size attribute.
        Args:
            size (int): The size of the new square"""

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
            else:
                raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
