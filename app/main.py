# app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models.base import Base
from .controllers.user import router as user_router
from .controllers.entry import router as entry_router

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Инициализация FastAPI
app = FastAPI()

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Подключение роутеров
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(entry_router, prefix="/entries", tags=["entries"])

# Простой эндпоинт для проверки работы сервера
@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Diary API!"}