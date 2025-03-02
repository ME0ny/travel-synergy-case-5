from sqlalchemy.orm import Session
from ..models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_telegram_id(self, telegram_id: str):
        return self.db.query(User).filter(User.telegram_id == telegram_id).first()

    def create_user(self, telegram_id: str, username: str = None):
        new_user = User(telegram_id=telegram_id, username=username)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user