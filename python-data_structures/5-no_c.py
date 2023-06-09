#!/usr/bin/python3
def no_c(my_string):
    str2 = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str2 += i
    return (str2)
