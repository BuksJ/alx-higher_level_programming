#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """return file and a string append it"""
    with open(filename, 'a', encoding='utf-8') as file:
        appended_text = file.write(text + '\n')
        file.closed
        return (appended_text)
