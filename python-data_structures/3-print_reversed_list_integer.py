#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    large = len(my_list)
    for i in range(large):
        print(my_list[large-i-1])
