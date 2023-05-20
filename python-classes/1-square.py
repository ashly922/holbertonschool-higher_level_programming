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
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.
        Args:
        size (int): The size of the square
        """
        self.__size = size
