from aiogram import Bot
from core import settings


bot = Bot(token=settings.botCfg.token)


async def send_new_order_to_bot(order_number: str, order_id: int) -> dict:
    try:
        await bot.send_message(
            text=f"Новый заказ с номером {order_number} и id = {order_id}",
            chat_id=int(settings.botCfg.chat_id)
        )
        return {
            "message": "Успешно отправлено сообщение"
        }
    except Exception as e:
        return {
            "message": f"Error: {e}"
        }