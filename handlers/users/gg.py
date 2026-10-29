# from aiogram import Router, types, F
#
# rt = Router()
#
# @rt.message(F.text)
# async def text(msg: types.Message):
#     await msg.answer("bu matn")
#
# @rt.message(F.photo)
# async def photo(msg: types.Message):
#     await msg.answer("bu rasm")
#
# @rt.message(F.voice)
# async def voice(msg: types.Message):
#     await msg.answer("bu voice")
#
# @rt.message(F.animation)
# async def animation(msg: types.Message):
#     await msg.answer("bu animation")
#
# @rt.message(F.contact)
# async def contact(msg: types.Message):
#     await msg.answer("bu contact")
#
# @rt.message(F.document)
# async def document(msg: types.Message):
#     await msg.answer("bu document")
#
# @rt.message(F.dice)
# async def dice(msg: types.Message):
#     await msg.answer("bu dice")
#
# @rt.message(F.location)
# async def location(msg: types.Message):
#     await msg.answer("bu location")
#
# @rt.message(F.venue)
# async def venue(msg: types.Message):
#     await msg.answer("bu venue")