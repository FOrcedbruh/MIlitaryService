from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
import asyncio
from settings import settings
import logging
import sys
from keyboards import main_keyboard
from api import requestHelper
from schemas import OrderInfoReadSchema
from requests import Response


dp = Dispatcher()


@dp.message(CommandStart())
async def index(message: Message) -> None:
    await message.answer(text=f"{message.from_user.full_name}, бот готов к работе", reply_markup=main_keyboard())


@dp.message()
async def index(message: Message) -> None:
    if (message.text == "Посмотреть все заказы"):
        orders: Response = requestHelper.get_orders()
        orders_json: list[OrderInfoReadSchema] = orders.json()
        for order_json in orders_json:
            await requestHelper.orders_response_form(**order_json, message=message)
        return
    if (message.text == "Последний заказ"):
        order: Response = requestHelper.get_last_order()
        order_json = order.json()
        await requestHelper.orders_response_form(**order_json, message=message)
        return
    else:
        await message.answer("Некорректная команда")


async def main() -> None:
    bot = Bot(token=settings.token,default=DefaultBotProperties())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())