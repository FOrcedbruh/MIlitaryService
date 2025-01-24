from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, CallbackQuery
import asyncio
from core import settings, logger
from keyboards import main_keyboard, order_numbers_keyboard
from clients import StoreClient
from helpers.states import OrderByNumberState
from presentation.OrderMessage import OrderFormatting


dp = Dispatcher()
bot = Bot(token=settings.token, default=DefaultBotProperties())

get_order_state = OrderByNumberState()

@dp.message(CommandStart())
async def index(message: Message) -> None:
    logger.info(f"Пользователь с id {str(message.from_user.id)} отправил команду /start")
    await message.answer(
        text=f"{str(message.from_user.full_name)}, бот готов к работе",
        reply_markup=main_keyboard()
    )


@dp.message(lambda message: message.text == "Посмотреть все заказы")
async def get_orders(message: Message) -> None:
    store_client = StoreClient(url=settings.store_base_url)
    logger.info(f"Пользователь с id ({str(message.from_user.id)}) нажал на кнопку 'посмотреть все заказы'")
    try:
        orders = store_client.get_all("orders/")
        print(orders)
    except Exception as e:
        await message.answer(f"Ошибка получения заказов: {e}")

@dp.message(lambda message: message.text == "Посмотреть подробности заказа")
async def check_info_by_order(message: Message) -> None:
    get_order_state.set_true()
    store_client = StoreClient(url=settings.store_base_url)
    logger.info(f"Пользователь с id ({str(message.from_user.id)}) нажал на кнопку 'Посмотреть подробности заказа'")
    orders: list[str] = store_client.get_numbers(endpoint="orders/numbers")
    await message.answer(
        text="Выберите номер заказа",
        reply_markup=order_numbers_keyboard(orders)
    )


@dp.message(lambda message: get_order_state.state == True)
async def get_order_by_number(message: Message):
    logger.info(f"Пользователь с id ({str(message.from_user.id)}) запросил заказ с номером {message.text}")
    get_order_state.set_false()
    store_client = StoreClient(url=settings.store_base_url)
    order_formatting = OrderFormatting()
    try:
        order = store_client.get_one(endpoint=f"orders/by_number?order_number={message.text}")
        content = order_formatting.get_content(order)
        await message.answer(**content.as_kwargs(), reply_markup=main_keyboard())
    except Exception as e:
        await message.answer(f"Ошибка получения заказа: {e}")


@dp.callback_query()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Бот запущен.")
    asyncio.run(main=main())