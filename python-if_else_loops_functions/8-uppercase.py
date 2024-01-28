#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            upper += chr(ord(ch) - 32)
        else:
            upper += ch
    print("{}".format(upper))
