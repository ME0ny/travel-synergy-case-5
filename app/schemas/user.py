# app/schemas/user.py

from pydantic import BaseModel

class UserBase(BaseModel):
    telegram_id: str
    username: str | None = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True