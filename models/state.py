#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """State Model"""

    __tablename__ = "states"

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities: Mapped["City"] = relationship("City", backref="state", cascade="delete")
