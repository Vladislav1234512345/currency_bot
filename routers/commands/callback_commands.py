
from aiogram import Router, F, types

from routers.commands.base_commands import get_text_currency
from routers.keyboards.keyboards_texts import values
from config import sum, currency

router = Router(name=__name__)




@router.callback_query(F.data == values.RUB_USD)
async def usd_rub_handle(callback_query: types.CallbackQuery):
    text = get_text_currency(callback_query.data)
    await callback_query.message.answer(
        text=text,
    )

@router.callback_query(F.data == values.RUB_EUR)
async def eur_rub_handle(callback_query: types.CallbackQuery):
    text = get_text_currency(callback_query.data)
    await callback_query.message.answer(
        text=text,
    )

@router.callback_query(F.data == values.USD_EUR)
async def rub_usd_handle(callback_query: types.CallbackQuery):
    text = get_text_currency(callback_query.data)
    await callback_query.message.answer(
        text=text,
    )

@router.callback_query(F.data == values.OTHER_CURRENCY)
async def rub_eur_handle(callback_query: types.CallbackQuery):
    text = "Enter your currencies down below:"
    await callback_query.message.answer(
        text=text,
    )