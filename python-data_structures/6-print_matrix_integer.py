#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print("")
        else:
            print(" ".join("{:d}".format(n) for n in row))
