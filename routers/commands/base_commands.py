from re import Match

from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.utils import markdown
from magic_filter import RegexpMode

from config import currency

from config import sum
def get_text_currency(information: types.CallbackQuery) -> str:
    number_first_value = sum.number
    values = information.upper().split("/")
    number_second_value = currency.convert(number_first_value, values[0], values[1])
    text = f"{number_first_value} {values[0]} = {number_second_value} {values[1]}"
    return text

router = Router(name=__name__)

@router.message(CommandStart())
async def start_handle(message: types.Message):
    text = markdown.text(
        markdown.text(
            "Hello, ",
            markdown.hitalic(f"{message.from_user.full_name}"),
            "!",
            sep="",
        ),
        markdown.text(
            "I am ",
            markdown.hbold("Currency Bot"),
            ". I count and compare the currencies between."
            "\nClick /help to know more information.",
            sep="",
        ),
        sep="\n",
    )
    await message.answer(
        text=text,
    )

@router.message(Command("help"))
async def help_handle(message: types.Message):
    description_text = ("I am Currency Bot. "
                        "My main task - provide you comfort counting and comparing different currencies between.")
    commands_text = ("\n/start - enable the bot"
            "\n/help - navigate the user"
            "\n/currency - count and compare currencies between")
    text = description_text + "\n" + commands_text
    await message.answer(
        text=text,
    )

@router.message(Command("currency"))
async def currency_handle(message: types.Message):
    await message.answer(
        text="Write the sum down below: ",
    )

@router.message(
    F.text.regexp(r"\b\w{3}\b/\b\w{3}\b", mode=RegexpMode.MATCH)
)
async def other_currency_handle(message: types.Message):
    text = get_text_currency(message.text)
    await message.answer(
        text=text,
    )
