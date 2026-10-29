from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

rt = Router()

@rt.message(Command("me"))
async def cmd_me(message: Message):
    user = message.from_user

    first_name = user.first_name
    last_name = user.last_name if user.last_name else "Kiritilmagan"
    username = f"@{user.username}" if user.username else "Mavjud emas"
    user_id = user.id

    text = (
        f"👤 Sizning profilingiz:**\n\n"
        f"🔹 Ism: {first_name}\n"
        f"🔹 Familiya: {last_name}\n"
        f"🔹 Username: {username}\n"
        f"🔹 Telegram ID: `{user_id}`"
    )

    await message.answer(text, parse_mode="Markdown")