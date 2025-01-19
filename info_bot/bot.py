from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, CallbackQuery
import asyncio
from core import settings, logger
from keyboards import main_keyboard
from clients import StoreClient


dp = Dispatcher()
bot = Bot(token=settings.token, default=DefaultBotProperties())



@dp.message(CommandStart())
async def index(message: Message) -> None:
    logger.info(f"Пользователь с id {str(message.from_user.id)} отправил команду /start")
    await message.answer(
        text=f"{str(message.from_user.full_name)}, бот готов к работе",
        reply_markup=main_keyboard()
    )


@dp.message()
async def get_orders(message: Message) -> None:
    logger.info(f"Пользователь с id {str(message.from_user.id)}) нажал на кнопку 'посмотреть все заказы'")
    store_client = StoreClient(url=settings.store_base_url)
    if message.text == "Посмотреть все заказы":
        try:
            orders = store_client.get_all(endpoint="orders/")
            print(orders)
        except Exception as e:
            await message.answer(f"Ошибка получения заказов: {e}")


@dp.callback_query()


async def main() -> None:
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Бот запущен.")
    asyncio.run(main=main())