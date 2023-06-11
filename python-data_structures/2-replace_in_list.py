#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
   
    new_list = my_list
    

    for i in my_list:
        if idx > len(my_list) - 1 or idx < 0:
            return my_list

        if my_list[i] == my_list[idx]:
            new_list[i] = element
            return new_list
