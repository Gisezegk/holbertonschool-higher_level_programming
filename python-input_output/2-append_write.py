#!/usr/bin/python3
"""append function"""


def append_write(filename="", text=""):
    """function append"""
    with open(filename, mode="a", encoding="utf-8") as f:
        read_file = f.write(text)

    return read_file
