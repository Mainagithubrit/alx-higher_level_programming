#!/usr/bin/python3

"""a python file that contains the class definition
of a State and an instance Base = declarative_base()"""

from sqlalchemy import BigInteger, Column, False_, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

MyMetadata = MetaData()
Base = declarative_base(metadata=MyMetadata)


class State(Base):
    """A class defining an id an name attributes of each state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
