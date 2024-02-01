#!/bin/usr/python3
def search_replace(my_list, search, replace):
    new_ls = my_list.copy()
    for i, number in enumerate(new_ls):
        if number == search:
            new_ls[i] = replace
    return new_ls
