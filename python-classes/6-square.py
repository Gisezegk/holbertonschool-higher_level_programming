#!/usr/bin/python3
"""
5-square.py:
Class Square that defines a square
"""


class Square:
    """
    Create an object of class Square
    """
    def __init__(self, size=0, position=(0, 0)):

        """
        Initialize square

        Attributes:
            size: private attribute size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter

        Return:
            size od square
        """
        return self.__size

    @property
    def position(self):
        """
        Getter

        Return:
            position to start printing square
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Setter

        Attributes:
            Value: the new position
        """
        self.__position = value
        if type(value) is not tuple or len(value) != 2 \
            or type(value[0]) is not int or type(value[1]) is not int \
            or value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
    
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
        with spaces given by position
        """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print()
            for row in range(self.size):
                for lines in range(self.position[0]):
                    print(" ", end='')
                for column in range(self.size):
                    print("#", end='')
                print()
