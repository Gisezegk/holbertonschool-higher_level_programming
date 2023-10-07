#!/usr/bin/python3
"""
Module 1-mylist
"""
class MyList(list):
    """
    class that inherits from list
    """
    def print_sorted(self):
        order_sort = sorted(self)
        print(order_sort)
