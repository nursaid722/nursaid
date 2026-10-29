from aiogram import Router, types, filters

rt = Router()

@rt.message(filters.Command("id_korish"))
async def id_korish(message: types.Message):
    await message.answer(f"🔹 sizning id raqamingiz: {message.from_user.id}")