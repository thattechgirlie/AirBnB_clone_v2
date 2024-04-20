#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


storage_type = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel):
    """ Review classto store review information """
    if storage_type == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
