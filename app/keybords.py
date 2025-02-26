from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item, get_item

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакти'), KeyboardButton(text='Про нас.')]],
    resize_keyboard=True,
    input_field_placeholder='Виберіть пункт меню...')


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:  # adding buttons
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
        # callback_data: це те, що отримає бот після натискання на кнопку.
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()  # створюємо клавіатуру.
    # adjusts(2) - кнопки будуть по 2 в ряд.
    # as_markup() - converts the InlineKeyboardBuilder object into InlineKeyboardMarkup
    # which can be sent as part of a message by the bot


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:  # adding buttons
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
        # callback_data: це те, що отримає бот після натискання на кнопку.
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def item(item_id):
    item = await get_item(item_id)
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='В корзину', callback_data='to_main'))
    return keyboard.as_markup()
