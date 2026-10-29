from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("bot_haqida"))
async def bot_haqida(msg: types.Message):
    await msg.answer("Bu bot al-fargoniy beckend dasturlashda yasalgan bot ")
