from bot import dp, bot
from aiogram import types
from . import text
from .credentials import USER_ID
from .filters import IsAdmin, IsUser, IsReply

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text.START)

@dp.message_handler(IsUser())
async def message_handler(message: types.Message):
    forward_message = await bot.forward_message(USER_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(USER_ID, message.chat.id, reply_to_message_id=forward_message.message_id) # Sends if bot can not get forward message chatid
    await message.answer(text.WAIT)


@dp.message_handler(IsAdmin(), IsReply())
async def answer_to_client(message: types.Message):
    chat_id = message.reply_to_message.text

    try:
        await bot.send_message(chat_id, message.text)
        await message.answer("Yuborildi!")
    except:
        await message.answer("Xatolik!")

