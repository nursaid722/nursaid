import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError,TelegramUnauthorizedError
from config.settings import BOT_TOKEN
from handlers.users.start import rt as start
from handlers.users.info import rt as help
from handlers.users.beckend import rt as beckend
from handlers.users.bot_haqida import rt as bot_haqida
from handlers.users.help import rt as info
from handlers.users.jorabek import rt as jorabek
from handlers.users.me import rt as me
from handlers.users.cobalt import rt as cobalt
from handlers.users.nexia_2 import rt as nexia_2
from handlers.users.rasm import rt as rasm
from handlers.users.reply import rt as reply
from handlers.users.delete import rt as delete
from handlers.users.answer_dice import rt as answer_dice
from handlers.users.ism_korish import rt as ism_korish
from handlers.users.tekshir import rt as tekshir
from handlers.users.date import rt as date
from handlers.users.pin import rt as pin
from handlers.users.mushuk import rt as mushuk
from handlers.users.it import rt as it
# from handlers.users.gg import rt as gg
# from handlers.users.contact import rt as contact
from handlers.users.type_top import rt as type_top
from handlers.users.dice_top import rt as dice_top




dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(start)
    dp.include_router(beckend)
    dp.include_router(bot_haqida)
    dp.include_router(help)
    dp.include_router(info)
    dp.include_router(jorabek)
    dp.include_router(me)
    dp.include_router(cobalt)
    dp.include_router(nexia_2)
    dp.include_router(rasm)
    dp.include_router(reply)
    dp.include_router(delete)
    dp.include_router(answer_dice)
    dp.include_router(ism_korish)
    dp.include_router(tekshir)
    dp.include_router(date)
    dp.include_router(pin)
    dp.include_router(mushuk)
    dp.include_router(it)
    # dp.include_router(gg)
    # dp.include_router(contact)
    dp.include_router(type_top)
    dp.include_router(dice_top)


    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi!")
    except TelegramNetworkError:
        print("internetga ulanmagansiz!")
    except TelegramUnauthorizedError:
        print("token xato!")
    except RuntimeError:
        print("roterlarda hatolik!")
