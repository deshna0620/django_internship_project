import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load env and Django
load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')
django.setup()

from mainapp.models import TelegramUser

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username or "Anonymous"
    TelegramUser.objects.get_or_create(username=username)
    await update.message.reply_text(f"Welcome {username}! You’ve been registered.")

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is polling...")
    app.run_polling()