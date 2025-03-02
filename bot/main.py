from bot.bot import setup_bot
import os

if __name__ == "__main__":
    TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
    if not TELEGRAM_API_KEY:
        raise ValueError("TELEGRAM_API_KEY is not set")

    application = setup_bot(TELEGRAM_API_KEY)
    application.run_polling()