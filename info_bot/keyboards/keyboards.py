from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def main_keyboard() -> ReplyKeyboardMarkup:
    kb_list: list = [
        [KeyboardButton(text="Посмотреть все заказы"), KeyboardButton(text="Посмотреть подробности заказа")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard

def order_numbers_keyboard() -> ReplyKeyboardMarkup:
    kb_list: list = [
        [KeyboardButton(text="12345678"), KeyboardButton(text="3421565")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard