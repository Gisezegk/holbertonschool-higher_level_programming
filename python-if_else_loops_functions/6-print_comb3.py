#!/usr/bin/python3
for i in range(0, 10):
    for g in range(0, 10):
        if i == g:
            continue
        if i > g:
            continue
        print("{}{}".format(i, g), end=", ")
