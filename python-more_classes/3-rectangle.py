#!/usr/bin/python3
"""."""


class Rectangle:
    """."""

    def __init__(self, width=0, height=0):
        """."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """."""
        return self.__width

    @width.setter
    def width(self, value):
        """."""
        if not isinstance(value, int):
            raise TypeError("Uzunluq int olmalidir")
        if value < 0:
            raise ValueError("Uzunluq sifirdan boyuk olmalidi")
        self.__width = value

    @property
    def height(self):
        """."""
        return self.__height

    @height.setter
    def height(self, value):
        """."""
        if not isinstance(value, int):
            raise TypeError("En int olmalidir")
        if value < 0:
            raise ValueError("En sifirdan boyuk olmalidir")
        self.__height = value

    def area(self):
        """."""
        return self.__width * self.__height

    def perimeter(self):
        """."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)
