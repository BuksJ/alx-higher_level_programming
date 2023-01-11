#!/usr/bin/python3

import sys

    argv = sys.argv[1:]

    if len(argv) == 0:
        print("Number of argument(s): 0.")
    else:
        print("Number of argument(s):", len(argv), end=".\n")
        for i in range(len(argv)):
            print(i+1, ":", argv[i], end='\n')
