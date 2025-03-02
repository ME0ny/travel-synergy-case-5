# bot/handlers/entry_handler.py

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
import requests
import os

# Состояния диалога
LOCATION, CATEGORY, IMAGE, DESCRIPTION = range(4)

# URL API
API_URL = "http://localhost:8000"
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

async def start_create_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начало создания записи."""
    await update.message.reply_text(
        "Пожалуйста, отправьте местоположение или укажите адрес.",
        reply_markup=ReplyKeyboardRemove()
    )
    return LOCATION

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка местоположения."""
    if update.message.location:
        latitude = update.message.location.latitude
        longitude = update.message.location.longitude
    else:
        address = update.message.text
        # TODO: Преобразовать адрес в координаты через Yandex Geocode API
        latitude, longitude = 0.0, 0.0  # Placeholder

    context.user_data["location"] = {"latitude": latitude, "longitude": longitude}
    await update.message.reply_text(
        "Выберите категорию:\n1. Cultural Heritage\n2. Place to Visit",
        reply_markup=ReplyKeyboardMarkup([["CulturalHeritage", "PlaceToVisit"]], one_time_keyboard=True)
    )
    return CATEGORY

async def handle_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка категории."""
    category = update.message.text
    if category not in ["CulturalHeritage", "PlaceToVisit"]:
        await update.message.reply_text("Неверная категория. Попробуйте снова.")
        return CATEGORY

    context.user_data["category"] = category
    await update.message.reply_text("Пожалуйста, отправьте изображение.")
    return IMAGE

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка изображения."""
    photo_file = await update.message.photo[-1].get_file()
    image_url = photo_file.file_path
    context.user_data["image_url"] = image_url

    await update.message.reply_text("Добавьте опциональное описание записи:")
    return DESCRIPTION

async def handle_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка описания."""
    description = update.message.text
    context.user_data["description"] = description

    # Отправка данных в API
    user_id = update.effective_user.id
    data = {
        "user_id": user_id,
        "location_latitude": context.user_data["location"]["latitude"],
        "location_longitude": context.user_data["location"]["longitude"],
        "image_url": context.user_data["image_url"],
        "category": context.user_data["category"],
        "description": context.user_data.get("description")
    }

    response = requests.post(f"{API_URL}/entries/create-entry", json=data)
    if response.status_code == 200:
        await update.message.reply_text("Запись успешно создана!")
    else:
        await update.message.reply_text("Произошла ошибка при создании записи.")

    return ConversationHandler.END

async def cancel_create_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отмена создания записи."""
    await update.message.reply_text("Создание записи отменено.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END