# app/models/entry.py

from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location_latitude = Column(Float, nullable=False)
    location_longitude = Column(Float, nullable=False)
    location_address = Column(String, nullable=True)
    image_url = Column(String, nullable=False)
    category = Column(Enum("CulturalHeritage", "PlaceToVisit", name="category_enum"), nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Связь с пользователем
    user = relationship("User", back_populates="entries")