# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка строки подключения
SQLALCHEMY_DATABASE_URL = "postgresql://travel_diary:travel_diary_password@localhost:5432/travel_diary_db"

# Создание движка SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовая модель
Base = declarative_base()