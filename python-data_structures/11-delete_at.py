#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = len(my_list)
    new_list = my_list
    if idx < 0 or idx > i - 1:
        return (my_list)
    else:
        if my_list:
            del my_list[3]
        return (new_list)
