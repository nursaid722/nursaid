# from aiogram import Router, types
#
# rt = Router()
#
#
# @rt.message()
# async def profile(msg: types.Message):
#
#     user = msg.from_user
#
#     if msg.chat.type == "private":
#         n = "Siz lichkadasiz!\n\n"
#         n += "O'zingiz haqingizda ma'lumot:\n"
#         n += f"ID: {user.id}\n"
#         n += f"Ismingiz: {user.first_name}\n"
#         n += f"Familiyangiz: {user.last_name or 'mavjud emas'}\n"
#         n += f"Username: @{user.username if user.username else 'mavjud emas'}\n"
#     else:
#         n = "Siz guruhdasiz!\n\n"
#         n += f"Guruh nomi: {msg.chat.title}\n"
#         n += f"Guruh ID: {msg.chat.id}\n\n"
#
#     await msg.answer(n)
