#!/usr/bin/python3
"""
test module for class Base
"""
import unittest
from models.base import Base

class Base(unittest.TestCase):
    def test_init_with_id(self):
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, Base._Base__nb_objects)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_data(self):
        data = [{'key': 'value'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"key": "value"}]')

    def test_save_to_file(self):
        obj = Base()
        Base.save_to_file([obj])
        with open('Base.json', 'r', encoding='utf-8') as f:
            json_str = f.read()
        self.assertEqual(json_str, '[{"id": 1}]')

    def test_from_json_string_empty_string(self):
        data = Base.from_json_string('')
        self.assertEqual(data, [])

    def test_from_json_string_with_data(self):
        json_str = '[{"key": "value"}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [{'key': 'value'}])

    def test_create_rectangle(self):
        rect = Base.create(id=1, width=3, height=4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)

    def test_create_square(self):
        square = Base.create(id=2, size=5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 5)

if __name__ == '__main__':
    unittest.main()
