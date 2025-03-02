# app/services/entry.py

from sqlalchemy.orm import Session
from ..models.entry import Entry
from ..schemas.entry import EntryCreate

def create_entry(db: Session, entry_data: EntryCreate):
    new_entry = Entry(
        user_id=entry_data.user_id,
        location_latitude=entry_data.location_latitude,
        location_longitude=entry_data.location_longitude,
        location_address=entry_data.location_address,
        image_url=entry_data.image_url,
        category=entry_data.category,
        description=entry_data.description
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_entries(db: Session, category: str | None = None):
    query = db.query(Entry)
    if category:
        query = query.filter(Entry.category == category)
    return query.all()

def get_entry_by_id(db: Session, entry_id: int):
    return db.query(Entry).filter(Entry.id == entry_id).first()