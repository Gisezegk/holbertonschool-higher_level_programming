#!/usr/bin/python3
"""
5-square.py:
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

    @property
    def size(self):
        """
        Getter

        Return:
            size od square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Attributes:
        Value: the new size
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public instance method that calculates the square area

        Return:
            area of the current sqauare
        """
        return(self.__size * self.__size)

    def my_print(self):
        """
        print a square made of '#'
        """
        if self.size == 0:
            print()
        else:
            for row in range(self.size):
                for column in range(self.size):
                    print("#", end='')
                print()
