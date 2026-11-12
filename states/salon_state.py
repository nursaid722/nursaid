from aiogram.fsm.state import State, StatesGroup

class AutoSalonState(StatesGroup):
    brend = State()
    model = State()
    yil = State()
    rang = State()