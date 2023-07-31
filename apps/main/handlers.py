from bot import dp, bot
from aiogram import types
from . import text
import os

USER_ID = os.environ.get("USER_ID") # set user_id to send messages to him.

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text.START)

@dp.message_handler()
async def message_handler(message: types.Message):
    await bot.send_message(USER_ID, message.text)
    await message.answer(text.WAIT)

