#!/usr/bin/python3
"""Module that contain a class Student"""


class Student:
    """ Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance with first_name,
           last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return student dictionary """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
