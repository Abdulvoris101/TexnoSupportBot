from bot import dp, bot
from aiogram import types
from . import text
from .credentials import USER_ID
from .filters import IsAdmin, IsUser, IsReplyFilter

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text.START)

@dp.message_handler(IsUser())
async def message_handler(message: types.Message):
    await bot.send_message(USER_ID, message.text)
    await message.answer(text.WAIT)


@dp.message_handler(IsAdmin(), IsReplyFilter())
async def answer_to_client(message: types.Message):
    await message.answer("YEAH")
