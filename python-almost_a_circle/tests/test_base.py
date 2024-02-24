#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_base_creation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_custom_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_rectangle_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    # Add more tests as needed


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
