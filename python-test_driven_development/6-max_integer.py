#!/usr/bin/python3
""" Task 6 """


def max_integer(list=[]):
    """ Task 6 """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
