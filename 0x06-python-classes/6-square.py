#!/usr/bin/python3
"""Define a class square"""


class Square:
    """ Define a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square's size and position.
        Args:
        size (int): size of the square.
        position (tuple): position of the square.
        """
    self.size = size
    self.position = position

    @property
    def size(self):
        """ Retrieve square's size.
        Returns:
        int: size of the square.
        """
    return self.__size

    @size.setter
    def size(self, value):
        """ Set square's size.
        Args:
        value (int): size of the square.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        @property
        def position(self):
            """ Retrieve square's position.
            Returns:
            tuple: position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set square's position

        Args:
        value (tuple): position of the square.
        Raises:
        TypeError: If position is not a tuple of 2 positive integers."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position")
