#!/usr/bin/python3
"""Task 5 - no more comments"""


def text_indentation(text):
    """Task 5 - no more comments"""
    error = "text must be a string"

    if not isinstance(text, str):
        raise TypeError(error)

    matches = [".", "?", ":"]
    i = 0

    while i < len(text):
        if text[i] in matches:
            print("{}\n\n".format(text[i]), end="")
            i += 1
            while text[i] == " ":
                i += 1
        else:
            print("{}".format(text[i]), end="")
            i += 1
