from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def main_keyboard() -> ReplyKeyboardMarkup:
    kb_list: list = [
        [KeyboardButton(text="Посмотреть все заказы"), KeyboardButton(text="Последний заказ")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard