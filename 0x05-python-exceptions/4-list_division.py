#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise ValueError("out of range")
            if not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            new_list.append(my_list_1[i] / my_list_2[i])
        except ValueError as v:
            print(v)
            new_list.append(0)
        except TypeError as t:
            print(t)
            new_list.append(0)
        except ZeroDivisionError as z:
            print(z)
            new_list.append(0)
            return (new_list)
