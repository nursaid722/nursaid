from aiogram import Router, types, F
from filters.admin import AdminFilter
rt = Router()
@rt.message(F.dice, AdminFilter())
async def start(msg: types.Message):
   await msg.answer("Botga xush kelibsiz")

