from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.new_chat_members)
async def new_chat_members(message: Message):
    new_members = ", ".join([user.full_name for user in message.new_chat_members])
    await message.reply(f"Guruhga xush kelibsiz, {new_members}!")
