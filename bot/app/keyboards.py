from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                             InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



#ne nuzno
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить данные')],
    [KeyboardButton(text='Помощь')], [KeyboardButton(text='Отмена')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункты меню')
#nuzno


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить', callback_data='Добавить')],
    [InlineKeyboardButton(text='Помощь', callback_data='Помощь')],
])

TypeS = [
    'Личное страхование',
    'Имущественное страхование',
    'Страхование ответственности'
    ]

async def inline_TypeS():
    keyboard = InlineKeyboardBuilder()
    for t in TypeS:
        keyboard.add(InlineKeyboardButton(text=t, callback_data=t))
    return keyboard.adjust(1).as_markup()