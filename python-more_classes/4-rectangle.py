#!/usr/bin/python3
"""
4-rectangle.py:
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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        resu = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        """
        for i in rangle(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result
        """
        resu = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return resu

    def __repr__(self):
        """
        new instance wit str
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
