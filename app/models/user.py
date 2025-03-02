# app/models/user.py

from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=True)

    # Связь с записями (entries)
    entries = relationship("Entry", back_populates="user")