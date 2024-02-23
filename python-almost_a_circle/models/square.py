#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """My Simple Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Get a string representation of the rectangle."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Get the size of the square"""
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value < 0:
            raise ValueError(f"width must be > 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Each argument to each attribute :D"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Return a dictionario representation of Square """
        square_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return square_dict