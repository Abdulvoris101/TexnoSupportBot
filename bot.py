from aiogram.dispatcher.dispatcher import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.environ.get("BOT_TOKEN"), parse_mode="HTML")

dp = Dispatcher(bot)