#!/usr/bin/python3
"""Task 4"""


def print_square(size):
    error = "size must be an integer"

    if (not isinstance(size, int) or
       (isinstance(size, float) and size < 0)):
        raise TypeError(error)

    if size < 0:
        raise ValueError("size must be >= 0")
    for element1 in range(size):
        for element2 in range(size):
            print("#", end="")
        print("")
