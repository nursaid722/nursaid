from aiogram import Router, types, filters, F
import random

rt = Router()

@rt.message(filters.Command("it"))
@rt.message(F.text.lower() == "it")
async def it(msg: types.Message):
    rasmlar = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbLy5hFEx78ZbNAzQoNEwJBFatPB4vysFrEhSqzapNfA&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQicdDPqI1mg_uIq2CUo_TJgdPjxhLTxKEF_1UFAXfa9w&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBHqicOz6t7SuXDK3xxDH9D6ZJ8vK3Gv08ecWci2fHew&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQSgP-XlWLq1QmPodM9SlVAYzbhaVzxZk3tIg0yBOgoA&s"
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_sH47dHBeNkmS6X97RaxgKrE_NzX4RHAZRkwvYggbcqyIi6WAqnLWngqK&s=10"
        ]
    rasm = random.choice(rasmlar)
    await msg.answer_photo(rasm)