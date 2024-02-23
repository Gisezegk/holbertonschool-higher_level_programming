#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """My Simple Rectangle Class"""
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """ special method: Constructor. Initialize the attributes. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value < 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the position."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the position."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """"Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle on the standard output."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Get a string representation of the rectangle."""
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}/{self.height}')

    def update(self, *args, **kwargs):
        """Update an argument to each attribute"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        for i, j in kwargs.items():
            setattr(self, i, j)

    def to_dictionary(self):
        """
            Return a represent of dictionario of Rectangle
        """
        rectangle_dict = {
            'y': self.y,
            'x': self.x,
            'id': self.id,
            'width': self.width,
            'height': self.height
        }
        return rectangle_dict