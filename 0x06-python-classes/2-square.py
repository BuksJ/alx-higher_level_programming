#!/usr/bin/python3
"""Defines a square by private instance attribute size
and instantiation with optional size
"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initialize a new square
        Args:
            size (int): size of the new square
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
