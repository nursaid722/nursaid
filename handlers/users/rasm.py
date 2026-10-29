from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("rasm"))
async def rasm(msg: types.Message):
    await msg.answer_photo("https://en.wikipedia.org/wiki/MrBeast")


