#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """Returns a dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @property
    def size(self):
        """tamaño del square"""
        return self.width

    @size.setter
    def size(self, value):
        """errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes using both args and kwargs."""
        if args:
            arg_count = len(args)
            if arg_count >= 1:
                self.id = args[0]
            if arg_count >= 2:
                self.size = args[1]
            if arg_count >= 3:
                self.x = args[2]
            if arg_count >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """defining self"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"