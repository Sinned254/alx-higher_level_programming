#!/usr/bin/python3
"""Module for the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """method accepts both *args (positional arguments)
        and **kwargs (keyword arguments).
        It checks if positional arguments are provided and assigns
        them in the specified order: id, size, x, y.
        If no positional arguments are provided or if keyword
        arguments are provided, it iterates through kwargs and
        assigns the key-value pairs to the corresponding attributes.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if not args or not kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary containing the id, size,
        x, and y attributes of the Square instance.
        This method allows you to easily convert a Square
        object into a dictionary representation.
        """
        return {
                 "id": self.id,
                 "size": self.size,
                 "x": self.x,
                 "y": self.y
                 }
