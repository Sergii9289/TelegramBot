from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keybords as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):  # перша функція після входу в бот /start
    await rq.set_user(message.from_user.id)  # передаємо user.id для перевірки існування юзера
    await message.answer('Ласкаво просимо в магазин взуття!', reply_markup=kb.main)


@router.message(F.text == 'Каталог')  # обробка сповіщеня 'Каталог'
async def catalog(message: Message):
    await message.answer('Виберіть категорію товару', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))  # обробка всіх запросів, що починаються на 'category_'
async def category(callback: CallbackQuery):
    category_id = int(callback.data.split('_')[1])
    cuurrent_category = await rq.get_category(category_id)
    await callback.message.answer(f'Оберіть товар з категорії {cuurrent_category}',
                                  reply_markup=await kb.items(category_id))


@router.callback_query(F.data.startswith('item_'))  # обробка всіх запросів, що починаються на 'item_'
async def item(callback: CallbackQuery):
    item_id = int(callback.data.split('_')[1])
    cuurrent_item = await rq.get_item(item_id)
    await callback.message.answer(f'Ви обрали товар:\nНазва: {cuurrent_item.name}\n'
                                  f'Опис: {cuurrent_item.description}\n'
                                  f'Ціна: {cuurrent_item.price}',
                                  reply_markup=await kb.item(item_id))
