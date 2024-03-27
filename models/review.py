#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Review(BaseModel, Base):
    """Review class to store review information """
    __tablename__ = "reviews"
    place_id: Mapped[str] = mapped_column(String(60), ForeignKey("places.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(String(60), ForeignKey("users.id"), nullable=False)
    text: Mapped[str] = mapped_column(String(1024), nullable=False)
