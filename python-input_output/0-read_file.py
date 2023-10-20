#!/usr/bin/python3
"""read files"""


def read_file(filename=""):
    """read file function"""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
