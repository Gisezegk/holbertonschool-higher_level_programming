#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i in range(96, 123):
            i -= 32
        print("{}".format(chr(i)), end="")
    print()
