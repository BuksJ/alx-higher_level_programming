#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # If the list is empty
        return None
    max_int = my_list[0]  # Initialize max_int with the first element of the list
    for i in my_list:
        if i > max_int:
            max_int = i
    return max_int
