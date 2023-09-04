#!/usr/bin/python3
""" Module has definatinion of class Rectangle
"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width(int):
            height(int):
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """width: returns width of rectangele

        Args:
            width (int): width in int
        Returns:
            wiidth
        Raises:
            TypeError: if width is not an ant int
            Valueerror: if width is less than o
        """
        return self.__width

    @property
    def height(self):
        """height: returns height
        Args:
            heigth (int): integer height of rectangle
        Returns:
            height of rectanle
        raises:
            TypeError: of height is not int
            valueError: of heigt is less than 0
        """
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
