from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from states.salon_state import AutoSalonState

rt = Router()


@rt.message(filters.Command("salon"))
async def start_salon(msg: types.Message, state: FSMContext):
    await msg.answer("Menga avtomobil brendini ayting (masalan: BMW, Mercedes, Chevrolet):")
    await state.set_state(AutoSalonState.brend)


@rt.message(AutoSalonState.brend)
async def brend_selected(msg: types.Message, state: FSMContext):
    await state.update_data(brend=msg.text)
    await msg.answer(f"{msg.text} tanlandi. Endi modelini kiriting (masalan: X5, M5, Cobalt):")
    await state.set_state(AutoSalonState.model)


@rt.message(AutoSalonState.model)
async def model_selected(msg: types.Message, state: FSMContext):
    await state.update_data(model=msg.text)
    await msg.answer("Zo'r! Endi ishlab chiqarilgan yilini kiriting (masalan: 2023, 2024):")
    await state.set_state(AutoSalonState.yil)


@rt.message(AutoSalonState.yil)
async def year_selected(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        yil_val = int(msg.text)
        if 1900 <= yil_val <= 2026:
            await state.update_data(yil=msg.text)
            await msg.answer("Endi o'zingizga yoqqan rangini ayting:")
            await state.set_state(AutoSalonState.rang)
        else:
            await msg.answer("Iltimos, realniy yilni kiriting (masalan: 2015, 2024):")
    else:
        await msg.answer("Yilni faqat raqamlarda kiriting:")


@rt.message(AutoSalonState.rang)
async def color_selected(msg: types.Message, state: FSMContext):
    await state.update_data(rang=msg.text)
    data = await state.get_data()

    brend = data.get("brend")
    model = data.get("model")
    yil = data.get("yil")
    rang = data.get("rang")

    await state.clear()

    domla = f"Barcha tanlovlaringiz qabul qilindi!\n\n"
    domla += f"Siz tanlagan mashina tafsilotlari:\n"
    domla += f"• Brend: {brend}\n"
    domla += f"• Model: {model}\n"
    domla += f"• Yili: {yil}\n"
    domla += f"• Rangi: {rang}"

    await msg.answer(domla)