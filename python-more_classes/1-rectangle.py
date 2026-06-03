#!/usr/bin/python3
"""baslayiriq"""


class Rectangle:
    """siniffff"""
    
    def __init__(self, width=0, height=0):
        """sss"""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ssss"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """S"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """SSsssS"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """SSSSS"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
