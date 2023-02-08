#!/usr/bin/python3
"""Module that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    # w = Truncate file to zero length or
    # create text file for writing
    with open(filename, mode="w", encoding="utf-8") as f:
        number_characters = f.write(text)
        # f.write(string) writes the contents
        # of string to the file
        # returning the number of characters written
        return (number_characters)
