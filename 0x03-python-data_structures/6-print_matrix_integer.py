#!/usr/bin/python3
x_integer(matrix=[[]]):
    for row in matrix:
    print(" ".join("{:d}".format(col) for col in row))   
