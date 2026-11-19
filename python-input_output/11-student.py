#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """A student defined by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the instance using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
