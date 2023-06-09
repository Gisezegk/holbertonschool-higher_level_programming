#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row, start=1):
            if i != 1:
                print("{}".format(" "), end="")
            print("{:d}".format(num), end=" ")
        print()
