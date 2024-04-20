#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
