#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    result = 0
    prev_value = 0


    for char in reversed(roman_string):
        if char not in roman_map:
            return 0
        curr_value = roman_map[char]
        result += curr_value if curr_value >= prev_value else -curr_value
        prev_value = curr_value
    return result
