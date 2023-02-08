#!/usr/bin/python3
"""a module that contains a function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Decoding JSON:"""
    return json.loads(my_str)
    # ['streaming API']
