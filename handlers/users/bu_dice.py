from aiogram import Router, types, F
from filters.admin import AdminGroupFilter
rt = Router()
@rt.message(F.dice, AdminGroupFilter())
async def dice(msg: types.Message):
   await msg.answer("bu dice")

