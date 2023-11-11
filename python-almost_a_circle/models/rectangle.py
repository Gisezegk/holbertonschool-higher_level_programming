#!/usr/bin/python3
"""comment something"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value is < 0:
            raise ValueError(f"width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """Get Height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if value is < 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x coor of the position"""
        return self.__x

    @x.setter
    def x(self, value):
        """set value of x coor"""
        if value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ set y coor of the position"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y coor of the position"""
       raise ValueError(f"y must be >= 0")
        self.__y = value
