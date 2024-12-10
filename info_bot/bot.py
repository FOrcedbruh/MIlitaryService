from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
import asyncio
from settings import settings
import logging
import sys
from keyboards import main_keyboard


dp = Dispatcher()



@dp.message(CommandStart())
async def index(message: Message) -> None:
    await message.answer(text=f"{message.from_user.full_name}, бот готов к работе", reply_markup=main_keyboard())


@dp.message()
async def index(message: Message) -> None:
    if (message.text == "Посмотреть все заказы"):
        await message.answer("Ваши заказы")
        return
    if (message.text == "Последний заказ"):
        await message.answer("Ваш последний заказ")
        return
    else:
        await message.answer("Некорректная команда")


async def main() -> None:
    bot = Bot(token=settings.token,default=DefaultBotProperties())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())