# bot/handlers/view_handler.py

import requests
from telegram import Update
from telegram.ext import ContextTypes

API_URL = "http://localhost:8000"

async def view_entries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Просмотр записей."""
    user_id = update.effective_user.id
    response = requests.get(f"{API_URL}/entries/view-entries")

    if response.status_code == 200:
        entries = response.json()
        if not entries:
            await update.message.reply_text("У вас пока нет записей.")
            return

        for entry in entries:
            message = (
                f"Location: {entry['location_address']}\n"
                f"Category: {entry['category']}\n"
                f"Description: {entry['description'] or 'No description'}\n"
            )
            await update.message.reply_photo(entry["image_url"], caption=message)
    else:
        await update.message.reply_text("Произошла ошибка при получении записей.")