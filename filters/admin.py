from aiogram import types, filters, Bot
from config.settings import ADMINS

class AdminFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return str(msg.from_user.id) in ADMINS

class AdminGroupFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message, bot):
        user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
        return user.status in ["creator", "administrator"]
