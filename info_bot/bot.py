from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, CallbackQuery
import asyncio
from settings import settings
import logging
import sys
from keyboards import main_keyboard
from utils import get_all_orders, get_last_order, get_order_by_id
from api import requestHelper

dp = Dispatcher()
bot = Bot(token=settings.token, default=DefaultBotProperties())


@dp.message(CommandStart())
async def index(message: Message) -> None:
    await message.answer(text=f"{message.from_user.full_name}, бот готов к работе, chat_id: {message.chat.id}", reply_markup=main_keyboard())


@dp.message()
async def index(message: Message) -> None:
    if (message.text == "Посмотреть все заказы"):
       await get_all_orders(message=message)
       return
    if (message.text == "Последний заказ"):
        await get_last_order(message=message)
        return
    else:
        await message.answer("Некорректная команда")
    return


@dp.callback_query()
async def view_data_by_callback(cq: CallbackQuery):
    info, order_id, order_number = cq.data.split(":")

    try:
        await cq.answer(text=f"Вот данные заказа с номером {order_number}")
        current_order = await get_order_by_id(order_id=order_id, order_number=order_number)
    except Exception:
        await bot.send_message(chat_id=int(settings.chat_id), text=requestHelper.INACTIVE)
        return

    answer_text: str = requestHelper.get_text_form_for_order(**current_order)
    await bot.send_message(chat_id=int(settings.chat_id), text=f"Данные заказа с номером {order_number}")
    await bot.send_message(chat_id=int(settings.chat_id), text=(answer_text), parse_mode="HTML")



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())