# app/services/user.py

from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate

def get_user_by_telegram_id(db: Session, telegram_id: str):
    return db.query(User).filter(User.telegram_id == telegram_id).first()

def create_user(db: Session, user_data: UserCreate):
    new_user = User(
        telegram_id=user_data.telegram_id,
        username=user_data.username
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user