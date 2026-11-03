from aiogram import F, Router
from aiogram.filters import Filter
from aiogram.types import Message

ADMIN_IDS = [123456789]
ADMIN_GROUP_ID = -100123456789

admin_router = Router()
admingroup_router = Router()
private_router = Router()
group_router = Router()


class IsAdmin(Filter):

  async def __call__(self, msg: Message) -> bool:
    return msg.from_user.id in ADMIN_IDS


class IsAdminGroup(Filter):

  async def __call__(self, msg: Message) -> bool:
    return msg.chat.id == ADMIN_GROUP_ID and msg.chat.type in [
        "group",
        "supergroup",
    ]


admin_router.message.filter(IsAdmin())
admingroup_router.message.filter(IsAdminGroup())
private_router.message.filter(F.chat.type == "private")
group_router.message.filter(F.chat.type.in_({"group", "supergroup"}))


@admin_router.message()
async def admin_func(msg: Message):
  await msg.answer("Salom admin!")


@admingroup_router.message()
async def admingroup_func(msg: Message):
  await msg.answer("Bu adminlar guruhi!")


@private_router.message()
async def private_func(msg: Message):
  await msg.answer("Salom, lichka!")


@group_router.message()
async def group_func(msg: Message):
  await msg.answer("Salom guruh!")