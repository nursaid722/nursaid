from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

router = Router()

ai_tugmalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ChatGPT", web_app=WebAppInfo(url="https://chatgpt.com")),
            InlineKeyboardButton(text="Gemini", web_app=WebAppInfo(url="https://gemini.google.com"))
        ],
        [
            InlineKeyboardButton(text="Claude", web_app=WebAppInfo(url="https://claude.ai")),
            InlineKeyboardButton(text="Grok", web_app=WebAppInfo(url="https://grok.com"))
        ]
    ]
)

@router.message(lambda message: message.text == "AI saytlar")
async def ai_saytlar_korsatish(message: types.Message):
    await message.answer("Sun'iy intellekt saytlaridan birini tanlang:", reply_markup=ai_tugmalar)