from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
import typing
from .credentials import USER_ID


class IsAdmin(BoundFilter):
    key = 'is_admin'

    async def check(self, message: types.Message) -> bool:
        return int(message.chat.id) == int(USER_ID)



class IsUser(BoundFilter):
    key = 'is_user'

    async def check(self, message: types.Message) -> bool:
        return int(message.chat.id) != int(USER_ID)



class IsReply(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.reply_to_message is not None:
            if message.reply_to_message.from_id != int(USER_ID):
                return True

        return False

