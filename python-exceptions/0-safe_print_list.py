#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ctr = 0
        for i in my_list:
            if ctr < x:
                print(i, end="")
                ctr += 1
            else:
                continue
        print()
        return ctr
    except TypeError:
        return 0
