from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keybords as kb
import app.database.requests as rq

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):  # перша функція після входу в бот /start
    await rq.set_user(message.from_user.id)  # передає мо user.id для перевірки існування юзера
    await message.answer('Ласкаво просимо в магазин взуття!', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вам потрібна допомога?')


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Оберіть категорію товара...', reply_markup=kb.catalog)


@router.callback_query(F.data == 'sneakers')
async def underpants(callback: CallbackQuery):
    await callback.answer('Ви обрали Кеди', show_alert=True)
    await callback.message.answer('Ви обрали категорію кеди.')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введіть ваше ім\'я')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введіть ваш вік')


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Введіть ваш номер телефону', reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваше ім\'я: {data['name']}\nВаш вік: {data['age']}\nВаш номер: {data['number']}")
    await state.clear()