from aiogram import Router, types, F
rt = Router()

@rt.message(F.photo)
async def photo(msg: types.Message):
    await msg.answer("Siz rasm tashadingiz")