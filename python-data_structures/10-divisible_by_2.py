#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_newlist = []
    for i in my_list:
        if (i % 2 == 0):
            my_newlist.append(True)
        else:
            my_newlist.append(False)
    return (my_newlist)
