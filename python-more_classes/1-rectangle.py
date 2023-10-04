#!/usr/bin/python3
"""
1-rectangle.py:
class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Create an object of class rectangle

    Attributes:
        height: height of the rectangle, private
        width: width of the rectangle, private
    both attributes must be integers >= 0
    """
    def __init__(self, width=0, height=0):

        """
        Initialize Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter

        Return:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Attributes:
        Value:  new width
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        Getter

        Return:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Attributes:
        value: new value
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mst be >= 0")
        
