#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """print an integer ({:d}".format()
    args:
    value (int): the integer to be printed
    Returns:
        if a TypeError or ValueError occurs - False
        otherwise - True
    """
    printed_elements = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                printed_elements += 1
            print()
    except:
        pass
        return printed_elements
