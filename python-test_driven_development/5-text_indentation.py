#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    char = ['.', ':', '?']

    for i in range(len(text)):
        if (text[i] in char):
            print("{}".format(text[i]))
            print()
        else:
            print("{}".format(text[i]), end="")
