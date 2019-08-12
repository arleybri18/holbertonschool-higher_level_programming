#!/usr/bin/python3
""" Model State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
""" Use https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/ """
Base = declarative_base()


class State(Base):
    """ Class State inherith from Base
    Implement model states """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref="state")
