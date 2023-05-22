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
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
        int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (int): Size of square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    self.__size = value

    def my_print(self):
        """
        Prints # squared
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

    def area(self):
        """
        Calculates and returns area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2


args = sys.argv[1:]


if args:

    try:
        size = int(args[0])
    except ValueError:
        size = 0

    my_square = Square(size)

    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
