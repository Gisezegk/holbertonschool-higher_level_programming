#!/usr/bin/python3
for i in range(10):
    for n in range(i + 1, 10):
        if i != n:
            if (i+n) != 17:
                print("{}{}".format(i, n), end=", ")
            elif (i+n) == 17:
                print("89")
