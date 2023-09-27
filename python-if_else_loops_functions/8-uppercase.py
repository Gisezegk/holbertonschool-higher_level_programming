#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper += chr(ord(char) - 32)
        else:
            upper += char
    print("{}".format(upper))
