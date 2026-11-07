from aiogram import Router
from aiogram.types import Message

rt = Router()

@rt.message()
async def reklama_ochir(msg: Message):
    if msg.entities or msg.caption_entities:
        try:
            await msg.delete()
        except:
            pass