from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("delete"))
async def delete(msg: types.Message):
    await msg.delete()
    await msg.answer("Ma'lumot ochirildi 😅 ")







