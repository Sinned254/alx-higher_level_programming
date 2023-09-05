#!/usr/bin/python3
""" Module has definatinion of class Rectangle
"""


class Rectangle:
    """Class Rectangle
    Attributes:
        number_of_instances (int)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width(int):
            height(int):
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
            raise TypeError("width must be an integer")
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

    def __str__(self):
        """string rep # of rectangle.
        Returns:
            string rep of rectangle
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        for r in range(self.height - 1):
            for c in range(self.width):
                string += str(self.print_symbol)
            string += '\n'
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """String rep of rectangle object"""
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """Delete Method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Returns the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares area of two rectangles and returns bigger area
        Args:
            rect_1: rectangle 1
            rect_2: rectangle 2
        Returns:
            larger area of the two rectangle areas
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a rectangle with square dimensions
        Args:
            size (int): dimensions of square rectangle
        Returns:
        rectangle object with square dimensions (size)
        """

        return cls(size, size)
