#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import os


class State(BaseModel, Base):
    """ State class """
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete")

    else:
        @property
        def cities(self):
            from . import storage
            from models.city import City
            my_cities = []
            cities_only = storage.all(City)
            for val in cities_only.values():
                if val.state_id == self.id:
                    my_cities.append(val)
            return my_cities
