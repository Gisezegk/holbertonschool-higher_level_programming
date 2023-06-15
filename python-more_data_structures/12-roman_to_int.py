#!/usr/bin/python3
def roman_to_int(roman_string):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    enteros = 0

    for i in range(len(roman_string)):
        if i > 0 and romanos[roman_string[i]] > romanos[roman_string[i - 1]]:
            enteros += romanos[roman_string[i]] - 2 * romanos[roman_string[i - 1]]
        else:
            enteros += romanos[roman_string[i]]
                       
    return enteros
