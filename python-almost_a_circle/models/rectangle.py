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
        return self._width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mst be > 0")
        self._height = value
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        """set x position coordenate"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """set y position coor"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value
