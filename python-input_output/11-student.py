#!/usr/bin/python3
"""Defines a Student class with reload functionality"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary.

        A dictionary key will be the public attribute name.
        A dictionary value will be the value of the public attribute.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
