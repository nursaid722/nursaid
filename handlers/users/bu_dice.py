from aiogram import Router, types, F
from filters.admin import AdminFilter
rt = Router()
@rt.message(F.dice, AdminFilter())
async def bu_dice(msg: types.Message):
   await msg.answer("bu dice")

