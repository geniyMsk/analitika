from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class keyboards():
    ready = ReplyKeyboardMarkup(
        keyboard=[
            [
               KeyboardButton(text='Я готов')
            ]
        ], resize_keyboard=True)

    sport = ReplyKeyboardMarkup(
        keyboard=[
            [
               KeyboardButton(text='Футбол ⚽')
            ],
            [
                KeyboardButton(text='Хоккей 🏒')
            ]
        ], resize_keyboard=True)