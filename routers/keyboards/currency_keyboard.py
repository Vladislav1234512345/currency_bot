from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .keyboards_texts import values

def currency_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=values.RUB_USD,
        callback_data=values.RUB_USD,
    )
    builder.button(
        text=values.RUB_EUR,
        callback_data=values.RUB_EUR,
    )
    builder.button(
        text=values.USD_EUR,
        callback_data=values.USD_EUR,
    )
    builder.button(
        text=values.OTHER_CURRENCY,
        callback_data=values.OTHER_CURRENCY,
    )
    builder.adjust(2)
    return builder.as_markup(
    )
