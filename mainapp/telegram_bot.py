import os
import sys
import django
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internship_project.settings")

django.setup()

from mainapp.models import TelegramUser

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

@sync_to_async
def create_telegram_user(username):
    return TelegramUser.objects.get_or_create(username=username)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    logger.info(f"Received /start command from user: {username}")

    if not username:
        await update.message.reply_text("Sorry, no username found in your Telegram profile.")
        return

    obj, created = await create_telegram_user(username)
    if created:
        await update.message.reply_text(f"Welcome {username}! You are now registered.")
    else:
        await update.message.reply_text(f"Welcome back {username}!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /start to register yourself.")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables.")
        return

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("Starting Telegram bot...")
    app.run_polling()

if __name__ == "__main__":
    main()