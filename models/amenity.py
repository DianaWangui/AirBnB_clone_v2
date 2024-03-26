#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, back_populates
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel):
    """ A place to stay """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place')
