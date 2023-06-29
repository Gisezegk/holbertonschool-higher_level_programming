#!/usr/bin/python3
"""
inherits Module
"""


def inherits_from(obj, a_class):
    """
    TRUE OR FALSE
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
