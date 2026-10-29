from aiogram import Router, filters, types, F

rt = Router()

@rt.message(F.sticker)
async def type_top(message: types.Message):
    await message.answer(f"{message.sticker.emoji} Stiker turi: `{message.sticker.type}`", parse_mode="Markdown")