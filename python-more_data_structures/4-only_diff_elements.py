#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif_1 = set_1 - set_2
    dif_2 = set_2 - set_1
    new_set = dif_1 | dif_2
    return new_set
