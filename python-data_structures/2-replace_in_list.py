#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    for i in my_list:
        if idx < 0:
            return (None)
        if idx < i:         
            return (None)
        if my_list[i] == my_list[idx]:
            new_list[i] = element
            return new_list
