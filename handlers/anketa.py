from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from states.anketa_state import AnketaState
from config.settings import Admins

rt = Router()


@rt.message(filters.Command("anketa"))
async def anketa(msg: types.Message, state: FSMContext):
    await msg.answer("Ismingizni kiriting:")
    await state.set_state(AnketaState.ism)


@rt.message(AnketaState.ism)
async def ism(msg: types.Message, state: FSMContext):
    await state.update_data(ism=msg.text)
    await msg.answer(f"{msg.text}, familyangizni kiriting:")
    await state.set_state(AnketaState.familya)


@rt.message(AnketaState.familya)
async def familya(msg: types.Message, state: FSMContext):
    fam = msg.text.strip().lower()
    if fam.endswith('a') or fam.endswith('v'):
        await state.update_data(familya=msg.text)
        await msg.answer("Yoshingizni kiriting:")
        await state.set_state(AnketaState.yosh)
    else:
        await msg.answer("Familyangiz 'a' yoki 'v' harfi bilan tugashi kerak. Iltimos, familyani qayta kiriting:")


@rt.message(AnketaState.yosh)
async def yosh(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        yosh_val = int(msg.text)
        await state.update_data(yosh=yosh_val)

        data = await state.get_data()
        user_ism = data.get("ism")
        user_fam = data.get("familya")
        fam_lower = user_fam.lower()

        if yosh_val == 20:
            murojaat = "Do'st"
        elif yosh_val > 20:
            if fam_lower.endswith('a'):
                murojaat = "Opa"
            else:
                murojaat = "Aka"
        else:
            if fam_lower.endswith('a'):
                murojaat = "Singil"
            else:
                murojaat = "Uka"

        await state.clear()

        n = f"Barcha ma'lumotlaringiz qabul qilindi, {murojaat}!\n\n"
        n += f"Siz haqingizda barcha ma'lumotlar:\n"
        n += f"Ism: {user_ism}\n"
        n += f"Familya: {user_fam}\n"
        n += f"Yosh: {yosh_val}\n"
        n += f"Maqom: {murojaat}"

        await msg.answer(n)
    else:
        await msg.answer("Yoshingizni faqat raqamlarda qayta kiriting!")