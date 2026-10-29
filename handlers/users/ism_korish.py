from aiogram import Router, filters, types

rt = Router()

@rt.message(filters.Command("ism_korish"))
async def ism_korish(msg: types.Message):
    ism = msg.from_user.first_name
    await msg.answer(f"Sizning ismingiz: {ism}")
