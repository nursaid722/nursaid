from aiogram import Router, types, filters
import datetime

rt = Router()


@rt.message(filters.Command("date"))
async def get_date(msg: types.Message):
    hozir = datetime.timedelta(hours=5) + msg.date
    yil = hozir.year
    oy = hozir.month
    kun = hozir.day
    soat = hozir.hour
    minut = hozir.minute
    sekund = hozir.second

    n = "Xabar yuborilgan sana va vaqt:\n"
    n += f"{yil}-{oy:02}-{kun:02} {soat:02}:{minut:02}:{sekund:02}\n"
    await msg.answer(n)