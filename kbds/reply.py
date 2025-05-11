from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Menu'),
        KeyboardButton(text='About'),
        KeyboardButton(text='Prod'),
        KeyboardButton(text='Payment'),
        ],
    ],
)