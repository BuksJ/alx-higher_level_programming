#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        while x:

            print(my_list[printed_elements], end=" ")
            printed_elements += 1
            x -= 1
    except:
        pass
    print()
    return (printed_elements)
