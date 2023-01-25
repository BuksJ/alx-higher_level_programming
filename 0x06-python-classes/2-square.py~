#!/usr/bin/python3

class Square:
    """
    Defines a square by private instance attribute size
    and instantiation with optional size
    """
    def __init__(self, size=0):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
