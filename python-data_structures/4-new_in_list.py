#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    
    new_list = my_list.copy()
    

    for i in new_list:
        if idx < 0 or idx > len(new_list) - 1:
            return new_list
    

        if new_list[i] == new_list[idx]:
            new_list[i] = element
            return new_list
