#!/usr/bin/python3
"""New square"""


class Square:
    """Define a square"""
    def __init__(self, size=0) -> None:
        if size < 0:
            raise ValueError("size must be >= 0")

        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

        else:
            self.__size = size
        pass
