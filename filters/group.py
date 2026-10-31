from aiogram import types, filters

class GroupFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return msg.chat.type in ["group","supergroup"]
