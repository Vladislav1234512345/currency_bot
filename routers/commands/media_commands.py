from aiogram import Router, types, F

from config import sum
from routers.keyboards.currency_keyboard import currency_keyboard

router = Router(name=__name__)


@router.message(F.text)
async def sum_handle(message: types.Message):
    try:
        sum.number = float(message.text)
        number = sum.number
        text = "Choose the currencies down below:"
        if number > 0:
            await message.answer(
                text=text,
                reply_markup=currency_keyboard(),
            )
        else:
            await message.answer(
                text="Number must be more than 0.",
            )
    except ValueError:
        await message.answer(
            text="Invalid type of currency. Try else one time.",
        )