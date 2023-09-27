#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    last_n = number % 10
    print(last_n, end="")
    return last_n
