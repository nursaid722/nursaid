from aiogram import Router, types, filters, F
import random

rt = Router()

@rt.message(filters.Command("mushuk"))
@rt.message(F.text.lower() == "mushuk")
async def mushuk(msg: types.Message):
    rasmlar = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsiVRM8FrteUeb3qw7wcm6oMKKmvZWMSj96y1FgdCRoA&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlWiLcDJX7oFjP2TPs-G5agaawZ-8TJlfaQKeCSoK7Kg&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr9rywgYKGwk0UXThRaHkOJeJSpAMttACOa1C_Gu24dQ&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTYjEnlPXiN-TjtmEQZQAYAlNsutw7wBYUwCpGpJPZzg&s=10",
    ]
    rasm = random.choice(rasmlar)
    await msg.answer_photo(rasm)