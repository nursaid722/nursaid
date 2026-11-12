
from aiogram.filters.state import State,StatesGroup

class AnketaState(StatesGroup):
    ism = State()
    familya = State()
    yosh = State()