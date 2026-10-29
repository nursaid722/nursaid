from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("nexia_2"))
async def nexia_2(msg: types.Message):
    await msg.answer("🔹 mashina modeli: Nexia 2\n"
                     "🔹 rangi:  oq\n"
                     "🔹 narxi: 3.400$\n"
                     "🔹 bosib otilgan masofasi: 134.000 km\n")

