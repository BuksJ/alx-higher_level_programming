#!/usr/bin/python3

"""
This is a class Square that defines a square with a private instance
attribute size, getter and setter method for size, and methods to calculate
the area and print the square.
"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Initialize a square with optional size."""
        self.size = size

        @property
        def size(self):
            """Getter method for the private attribute size."""
            return self.__size

        @size.setter
        def size(self, value):
            """Setter method for the private attribute size."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Method that returns the current square area"""
                return self.__size ** 2

        def my_print(self):
            """Method that prints in stdout the square with the character #."""
            if self.__size == 0:
                for i in range(self.__size):
                    for j in range(self.__size):
                        print("#", end="")

                    print()
