#!/usr/bin/python3
"""file wirten"""


def write_file(filename="", text=""):
    """write function"""
    with open(filename, mode="w", encoding="utf-8") as f:
        read_data = f.write(text)
        f.close

    return read_data
