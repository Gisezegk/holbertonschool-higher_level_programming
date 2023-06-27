#!/usr/bin/python3

"""
print a square function
"""
def print_square(size):
    

    if (type(size) != int) or (size < 0 and type(size) == float):
       TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#" * size))
