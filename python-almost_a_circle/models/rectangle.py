#!/usr/bin/python3
"""comment something"""

class Rectangle(Base):
    """
    rectangle class
    """
    def __init__(self, width, height, x=0, y=0):
        """
        init rectangle
        Attributes:
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        Value: new width
        """
        self.__width = value

