#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_a = sorted(a_dictionary.items())
    for key, val in sort_a:
        print("{}: {}".format(key, val))
