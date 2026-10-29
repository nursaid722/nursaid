from aiogram import Router, types, filters

rt = Router()

@rt.message(filters.Command("pinned"))
async def pinned_func(msg: types.Message):
    if msg.pinned_message:
        matn = msg.pinned_message.text or "Matn mavjud emas"
        await msg.answer(f"Pin qilingan xabar:\n{matn}")
    else:
        await msg.answer("Pin qilingan xabar topilmadi.")