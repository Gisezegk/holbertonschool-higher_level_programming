#!/usr/bin/python3
"""module 8-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """clase rectangulo?"""
    def __init__(self, width=0, height=0):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
