#!/usr/bin/python3
"""module 9-student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """inicialize atributtes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """json representation"""
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
        }
