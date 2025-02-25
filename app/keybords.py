from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакти'), KeyboardButton(text='Про нас.')]],
    resize_keyboard=True,
    input_field_placeholder='Виберіть пункт меню...')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кеди', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кросівки', callback_data='trainers')],
    [InlineKeyboardButton(text='Туфлі', callback_data='shoes')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Відправити номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)

