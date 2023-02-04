#!/usr/bin/python3
"""This is the addition module.
It adds 2 integers a and b must be first casted"""


def add_integer(a, b=98):
    """a and b are integers
    Returns an integer: the addition of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    return int(a) + int(b)
