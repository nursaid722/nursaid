from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message):
    await msg.answer("Botga xush kelibsiz")

