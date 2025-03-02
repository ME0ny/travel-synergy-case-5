# bot/bot.py

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)
from .handlers.entry_handler import (
    start_create_entry,
    handle_location,
    handle_category,
    handle_image,
    handle_description,
    cancel_create_entry,
)

def setup_bot(token: str):
    application = Application.builder().token(token).build()

    # Диалог создания записи
    create_entry_handler = ConversationHandler(
        entry_points=[CommandHandler("create_entry", start_create_entry)],
        states={
            LOCATION: [MessageHandler(filters.LOCATION | filters.TEXT, handle_location)],
            CATEGORY: [MessageHandler(filters.TEXT, handle_category)],
            IMAGE: [MessageHandler(filters.PHOTO, handle_image)],
            DESCRIPTION: [MessageHandler(filters.TEXT, handle_description)],
        },
        fallbacks=[CommandHandler("cancel", cancel_create_entry)],
    )

    application.add_handler(create_entry_handler)

    return application