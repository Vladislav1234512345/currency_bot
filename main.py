import asyncio
import logging

from aiogram import Dispatcher, Bot, types
from aiogram.enums import ParseMode

from config import settings
from routers import router as main_router

async def main():
    dp = Dispatcher()
    dp.include_router(main_router)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        parse_mode=ParseMode.HTML,
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
