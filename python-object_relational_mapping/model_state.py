#!/usr/bin/python3
"""Module that defines the State class and the Base instance."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class linked to the MySQL table states.

    Attributes:
        id (int): auto-generated primary key.
        name (str): the name of the state, up to 128 characters.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
