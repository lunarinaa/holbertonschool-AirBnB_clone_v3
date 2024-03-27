#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, ForeignKey, String

from models.base_model import Base, BaseModel

# Not implemented yet
# class Review(BaseModel, Base):
#     """ Review class to store review information """
#     __tablename__ = "reviews"
#     place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
#     user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
#     text = Column(String(60), nullable=False)
