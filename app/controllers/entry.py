# app/controllers/entry.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.entry import create_entry, get_entries, get_entry_by_id
from ..database import get_db
from ..schemas.entry import EntryCreate, Entry

router = APIRouter()

@router.post("/create-entry", response_model=Entry)
def create_entry_route(entry_data: EntryCreate, db: Session = Depends(get_db)):
    return create_entry(db, entry_data)

@router.get("/view-entries", response_model=list[Entry])
def view_entries_route(category: str | None = None, db: Session = Depends(get_db)):
    return get_entries(db, category)

@router.get("/view-entry/{entry_id}", response_model=Entry)
def view_entry_route(entry_id: int, db: Session = Depends(get_db)):
    entry = get_entry_by_id(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry