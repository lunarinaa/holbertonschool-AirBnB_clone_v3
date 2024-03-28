#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

import models
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.review import Review

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id: Mapped[str] = mapped_column(
        String(60), ForeignKey("cities.id"), nullable=False
    )
    user_id: Mapped[str] = mapped_column(
        String(60), ForeignKey("users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    number_rooms: Mapped[int] = mapped_column(default=0, nullable=False)
    number_bathrooms: Mapped[int] = mapped_column(default=0, nullable=False)
    max_guest: Mapped[int] = mapped_column(default=0, nullable=False)
    price_by_night: Mapped[int] = mapped_column(default=0, nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=True)
    longitude: Mapped[float] = mapped_column(nullable=True)
    reviews: Mapped["Review"] = relationship(
        "Review", backref="place", cascade="delete"
    )

    amenity_ids = []

    if os.getenv("DB_STORAGE_TYPE") != "db":

        @property
        def amenities(self):
            """Getter for amenities"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Setter for amenities"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
