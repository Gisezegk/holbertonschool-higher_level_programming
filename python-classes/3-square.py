#!/usr/bin/python3
"""
1-square.py:
Class Square that defines a square
"""


class Square:
    """
    Create an object of class Square
    """
    def __init__(self, size=0):

        """
        Initialize square

        Attributes:
            size: private attribute size of square
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public instance method that calculates the square area

        Return:
            area of the current sqauare
        """
        return(self.__size * self.__size)
