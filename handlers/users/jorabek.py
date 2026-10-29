from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("jorabek"))
async def jorabek(msg: types.Message):
    await msg.answer("🔹 yosh = 11\n"
                     "🔹 qiziqish = dasturlash\n"
                     "🔹 kasb = beckend developer\n"
                     "🔹 uy manzili = poshshopirim 34-uy\n")


