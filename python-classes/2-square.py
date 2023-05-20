#!/usr/bin/python3
"""
This module defines the Square class
The Square class represents a square shape
"""


class Square:
    """
    A class representing a square
    attributes:
        size (int): the size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
