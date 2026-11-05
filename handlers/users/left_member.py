from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.left_chat_member)
async def left_chat_member(message: Message):
    user = message.left_chat_member
    await message.reply(f"{user.full_name} guruhni tark etdi.")