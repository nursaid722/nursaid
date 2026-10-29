from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("beckend"))
async def beckend(msg: types.Message):
    print("Bot started")
    await msg.answer("dasturlashni 0 dan o'rganing "
                     "aloqa uchun 50-506-2211")
