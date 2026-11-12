from aiogram import Router, Bot
from aiogram.types import Message

rt = Router()

@rt.message()
async def reklama_ochir(msg: Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status in ["member"]:
        if msg.entities or msg.caption_entities:
            try:
                await msg.delete()
            except:
                pass