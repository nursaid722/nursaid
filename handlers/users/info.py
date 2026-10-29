from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("info"))
async def info(msg: types.Message):
    await msg.answer(".")
    n = "Bizning barcha funksiyalarimiz:\n"
    n += "🔹/help\n"
    n += "🔹/bot_haqida\n"
    n += "🔹/beckend\n"
    n += "🔹/cobalt\n"
    n += "🔹/nexia_2\n"
    n += "🔹/jorabek\n"
    n += "🔹/info\n"
    n += "🔹/me\n"
    n += "🔹/start\n"
    n += "🔹/rasm\n"
    n += "🔹/reply\n"
    n += "🔹/delete\n"
    n += "🔹/answer_dice\n"
    n += "🔹/id_korish\n"
    n += "🔹/ism_korish\n"
    n += "🔹/familya_korish\n"
    n += "🔹/tekshir\n"
    n += "🔹/date\n"
    n += "🔹/pin\n"
    n += "🔹/mushuk\n"
    n += "🔹/it\n"
    n += "🔹/type_top\n"
    await msg.answer(n)

 