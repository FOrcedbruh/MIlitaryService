from aiogram import Bot
from core import settings
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ...schemas import OrderInfoReadSchema

bot = Bot(token=settings.botCfg.token)

def inline_keyboard(order_id: int, order_number: str) -> InlineKeyboardMarkup:
    button = InlineKeyboardButton(text="Посмортеть данные заказа", callback_data=f"View order data:{order_id}:{order_number}")
    return InlineKeyboardMarkup(inline_keyboard=[[button]], resize_board=True)

async def send_new_order_to_bot(order_number: str, order_id: int) -> dict:
    try:
        await bot.send_message(
            text=f"🎉Новый заказ с номером {order_number} оформлен🎉",
            chat_id=int(settings.botCfg.chat_id),
            reply_markup=inline_keyboard(order_id=order_id, order_number=order_number)
        )
        return {
            "message": "Успешно отправлено сообщение"
        }
    except Exception as e:
        return {
            "message": f"Error: {e}"
        }

def order_response_for_bot(order_in: OrderInfoReadSchema) -> OrderInfoReadSchema:
    return OrderInfoReadSchema(
        order_number=order_in.order_number,
        cost_sum=order_in.cost_sum,
        address=order_in.address,
        delivery_type=order_in.delivery_type,
        payment_type=order_in.payment_type,
        is_paid=order_in.is_paid,
        customer_email=order_in.customer_email,
        customer_phone=order_in.customer_phone,
        customer_name=order_in.customer_name,
        products=order_in.products,
        created_at=order_in.created_at
    )
