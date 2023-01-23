#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """print an integer ({:d}".format()
    args:
    value (int): the integer to be printed
    Returns:
        if a TypeError or ValueError occurs - False
        otherwise - True
    """
    integers_printed = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                integers_printed += 1
        except:
            raise Exception("x is bigger than the length of my_list")
        print ()
        return integers_printed
