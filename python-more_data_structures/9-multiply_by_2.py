#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    my_dict.update((key, value * 2) for key, value in my_dict.items())
    return my_dict
