from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.new_chat_photo)
async def handle_new_chat_photo(message: Message):
    await message.reply("Guruh profili uchun yangi rasm qo`yildi!")