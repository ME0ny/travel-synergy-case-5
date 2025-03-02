from sqlalchemy.orm import Session
from ..models.entry import Entry

class EntryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_entry(self, user_id: int, location_latitude: float, location_longitude: float, location_address: str, image_url: str, category: str, description: str = None):
        new_entry = Entry(
            user_id=user_id,
            location_latitude=location_latitude,
            location_longitude=location_longitude,
            location_address=location_address,
            image_url=image_url,
            category=category,
            description=description
        )
        self.db.add(new_entry)
        self.db.commit()
        self.db.refresh(new_entry)
        return new_entry

    def get_entries_by_user_id(self, user_id: int):
        return self.db.query(Entry).filter(Entry.user_id == user_id).all()