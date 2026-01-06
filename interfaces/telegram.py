from telegram.ext import Application, MessageHandler, filters
from core.ai import ask_ai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def handle(update, context):
    text = update.message.text
    reply = ask_ai(text)
    await update.message.reply_text(reply)

def run_telegram():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("Bot started...")
    app.run_polling()
