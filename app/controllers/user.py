# app/controllers/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.user import get_user_by_telegram_id, create_user
from ..database import get_db
from ..schemas.user import UserCreate
from ..models.user import User

router = APIRouter()

@router.post("/auth", response_model=User)
def authenticate_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = get_user_by_telegram_id(db, user_data.telegram_id)
    if not user:
        return create_user(db, user_data)
    return user