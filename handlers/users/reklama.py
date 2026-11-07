from aiogram import Router, F, types

rt = Router()


@rt.message(F.chat.type.in_({"group", "supergroup"}))
async def reklama_ochir(msg: types.Message):
    text = msg.text or msg.caption

    if text:
        if "http" in text or "t.me" in text or "@" in text:
            try:
                await msg.delete()
            except:
                pass
