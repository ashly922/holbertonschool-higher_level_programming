#!/usr/bin/python3
"""
This module provides a method that adds two integers    
"""
def add_integer(a, b=98):
    """
    Adds two integers and returns the sum

    Args:
        a (int or float)
        b (int or float)

    Raises:
        TypeError: if a or b is not an int or float

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    sum = a + b

    return int(sum)
