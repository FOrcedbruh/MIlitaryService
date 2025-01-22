from aiogram.utils.formatting import (
    Bold, as_list, as_section, as_key_value, as_marked_section, Text
)
from dto.orders import OrderReadSchema
from datetime import datetime


class OrderFormatting():
    
    def get_content(self, order: OrderReadSchema) -> Text:
        content = as_list(
            as_section(
                Bold("ℹ️ Заказ"),
            ),
            as_section(
                as_key_value("Номер заказа:", order["order_number"]),
                as_key_value("Заказчик:", order["customer_name"]),
                as_key_value("Почта заказчика:", order["customer_email"]),
                as_key_value("Телефон:", order["customer_phone"]),
                as_key_value("Статус оплаты", order["is_paid"])
            ),
            as_marked_section(
                Bold("Инфоормация о заказа:"),
                as_key_value("Сумма заказа", order["cost_sum"]),
                as_key_value("Тип оплаты", order["payment_type"]),
                as_key_value("Тип получения заказа", order["delivery_type"]),
                as_key_value("Адрес доставки", order["address"]),
                marker="  "
            ),
            as_marked_section(
                Bold("Дата оформления", self.format_date(order["created_at"])),
                marker="🕰 "
            ),
            sep="\n\n"
        )
        return content

    def format_date(self, date: datetime) -> str:
        # return str(date)[-15].replace("-", ":") + "года" + "в" + str(date)[-9:-6]
        return str(date)


    