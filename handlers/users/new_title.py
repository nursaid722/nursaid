from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.new_chat_title)
async def handle_new_chat_title(message: Message):
    new_title = message.new_chat_title
    await message.reply(f"Guruh nomi yangilandi: <b>{new_title}</b>", parse_mode="HTML")