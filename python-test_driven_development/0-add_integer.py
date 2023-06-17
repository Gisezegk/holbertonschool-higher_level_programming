#!/usr/bin/python3
"""
add_integer - function for adding 2 int numbers
a: first input number
b: second input number
"""


def add_integer(a, b=98):
    """
    Check if a and b are float or int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
