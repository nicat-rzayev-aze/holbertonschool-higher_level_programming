#!/usr/bin/python3
"""Defines a Student class with filter."""


class Student:
    """A class that defines a student"""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Return a dictionary representation of a student."""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
