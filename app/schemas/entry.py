# app/schemas/entry.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EntryBase(BaseModel):
    location_latitude: float
    location_longitude: float
    location_address: Optional[str] = None
    image_url: str
    category: str
    description: Optional[str] = None

class EntryCreate(EntryBase):
    user_id: int

class Entry(EntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True