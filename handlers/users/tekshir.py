from aiogram import Router, filters, types

rt = Router()

@rt.message(filters.Command("tekshir"))
async def tekshir(msg: types.Message):
    if msg.from_user.is_bot:
        await msg.answer("🔹Siz botsiz!")
    else:
        await msg.answer("🔹Siz oddiy foydalanuvchisiz.")
