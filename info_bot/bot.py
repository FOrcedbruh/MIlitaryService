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
        try:
            orders: Response = requestHelper.get_orders()
            orders_json: list[OrderInfoReadSchema] = orders.json()
            if (orders.status_code != 200):
                await requestHelper.error_response_form(message=message, error_reason=orders.reason, status_code=orders.status_code)
                return
            await message.answer(text="Вот все текущие и завершенные заказы 📦")
            for order_json in orders_json:
                await requestHelper.orders_response_form(**order_json, message=message)
            return
        except Exception:
            await message.answer(text=requestHelper.INACTIVE)
            return
        
    if (message.text == "Последний заказ"):
        try:
            order: Response = requestHelper.get_last_order()
            if (order.status_code != 200):
                await requestHelper.error_response_form(message=message, error_reason=order.reason, status_code=order.status_code)
                return
            order_json = order.json()
            await message.answer(text="Последний оформленный заказ ⏳")
            await requestHelper.orders_response_form(**order_json, message=message)
            return
        except Exception:
            await message.answer(text=requestHelper.INACTIVE)
    else:
        await message.answer("Некорректная команда")
    return
        
        

async def main() -> None:
    bot = Bot(token=settings.token, default=DefaultBotProperties())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())