from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("cobalt"))
async def cobalt(msg: types.Message):
    await msg.answer("🔹 mashina modeli: cobalt\n"
                     "🔹 rangi:  qora\n"
                     "🔹 narxi: 10.500$\n"
                     "🔹 probegi: 12.000 km\n")


