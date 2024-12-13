from requests import Response
import requests
from aiogram.types import Message
import aiogram.utils.markdown as fmt
from settings import settings

class RequestsHelper():
    def get_orders(self) -> Response:
        res: Response = requests.get(url=settings.base_url + "orders/info")

        return res

    def get_last_order(self) -> Response:
        res: Response = requests.get(url=settings.base_url + "orders/last_order")

        return res

    async def orders_response_form(
        self, order_number: str,
        address: str, 
        delivery_type: str, 
        payment_type: str, 
        is_paid: str, 
        message: Message,
        cost_sum: int,
        customer_phone: str,
        customer_email: str,
        customer_name: str,
        created_at: str,
        products: str
    ):
        products_list: str = ""
        for i, product in enumerate(products):
            products_list += f"{i + 1}. {product}\n"
        await message.answer(text=(
            fmt.text(
                fmt.text(fmt.hbold(f"Номер заказа: {order_number}")),
                fmt.text(fmt.hunderline(f"Адрес доставки: {address}")),
                fmt.text(f"Доставка: {delivery_type}"),
                fmt.text(f"Оплата: {payment_type}"),
                fmt.text(f"Статус оплаты: {"Оплачено" if is_paid == True else "Не оплачено"}"),
                fmt.text(f"Общая стоимость: {cost_sum}"),
                fmt.text(f"Телефон заказчика: {customer_phone}"),
                fmt.text(f"Почта заказчика: {customer_email}"),
                fmt.text(f"Имя заказчика: {customer_name}\n"),
                fmt.text(
                    fmt.text(fmt.hbold("Товары: \n")),
                    fmt.text(products_list),
                ),
                fmt.text(f"Заказ оформлен {created_at}"),
                sep="\n"
            )
        ), parse_mode="HTML")
        return


requestHelper = RequestsHelper()