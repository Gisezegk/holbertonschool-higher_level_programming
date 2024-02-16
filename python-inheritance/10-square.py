#!/usr/bin/python3
"""module 10-square"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """clase square rectangulo"""
    def __init__(self, size):
        """Intialize a rectangule"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area"""
        return self.__size ** 2
