#!/usr/bin/python3
"""
Empty class
"""


class BaseGeometry():
    """
    Base Geometry
    """

    def area(self):
        raise Exception("are() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 1:
            raise ValueError("{} must be greater than 0".format(name))
