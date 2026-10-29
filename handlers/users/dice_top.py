from aiogram import Router, types

rt = Router()


@rt.message()
async def dice_top(msg: types.Message):
    if msg.dice:
        if msg.dice.emoji == "🎳":
            n = f"bowling da {msg.dice.value} uriladi"
        else:
            n = f"ushbu {msg.dice.emoji} ning qiymati 100%\n"
            n += f"{msg.dice.value} bo'ladi!"
        await msg.answer(n)
    elif msg.animation:
        print(msg.animation)