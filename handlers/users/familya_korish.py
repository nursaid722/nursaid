from aiogram import Router, filters, types

rt = Router()

@rt.message(filters.Command("familya_korish"))
async def familya_korish(msg: types.Message):
    familiya = msg.from_user.last_name
    if familiya:
        await msg.answer(f"🔹Sizning familiyangiz: {familiya}")
    else:
        await msg.answer("🔹Siz profilga familiya kiritmagansiz.")