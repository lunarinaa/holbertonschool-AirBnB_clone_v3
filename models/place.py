#!/usr/bin/python3
""" Place Module for HBNB project """
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'

    city_id: Mapped[str] = mapped_column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id: Mapped[str] = mapped_column(String(60), ForeignKey('users.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    number_rooms: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    number_bathrooms: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    max_guest: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    price_by_night: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=True)
    reviews: Mapped["Review"] = relationship("Review", backref="place", cascade="delete")

