#!/usr/bin/python3
"""
    class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py).
    Instantiation with width and height:
    def __init__(self, width, height):
        width and height must be private.
        No getter or setter
        width and height must be positive integers,
        validated by integer_validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class inherits from basegeometry """

    def __init__(self, width, height):
        """ initialization """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns area of self"""
        return self.__width * self.__height
