from telegram.ext import Application, MessageHandler, filters
from dotenv import load_dotenv
from core.ai import ask_ai, analyze
from core.intents import validate_intent
from core.dispatcher import dispatch
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update, context):
    user_text = update.message.text

    try:
        ai_data = analyze(user_text)
        intent = validate_intent(ai_data)
        response = dispatch(intent)
    except Exception as e:
        response = f"⚠️ Error: {e}"

    await update.message.reply_text(response)


def run_telegram():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🤖 Telegram AI bot is running...")
    app.run_polling()
    
async def handle(update, context):
    text = update.message.text
    reply = ask_ai(text)
    await update.message.reply_text(reply)

def run_telegram():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("Bot started...")
    app.run_polling()
