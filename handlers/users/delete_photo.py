from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.delete_chat_photo)
async def handle_delete_chat_photo(message: Message):
    await message.reply("Guruh profili rasmi o'chirildi.")