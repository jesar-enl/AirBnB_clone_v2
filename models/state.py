#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
import os


store = os.getenv('HBNB_TYPE_STORAGE')
class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if store == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """getter attribute"""
        from models import storage
        lista = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                lista.append(city)
        return lista
