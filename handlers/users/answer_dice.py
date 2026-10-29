
from aiogram import Router, filters, types

rt = Router()

@rt.message(filters.Command("answer_dice"))
async def answer_dice(msg: types.Message):
    await msg.answer_dice(emoji="🎲")

