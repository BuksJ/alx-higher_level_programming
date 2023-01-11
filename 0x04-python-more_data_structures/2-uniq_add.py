#!/usr/bin/python3

def uniq_add(my_list=[]):
    return sum(set(x for x in my_list if isinstance(x, int)))
