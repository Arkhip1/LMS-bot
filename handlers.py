from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboards as kbs

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    fav_color = State()


@router.message(CommandStart())
async def cmnd_strt(message: Message, state: FSMContext):
    await message.answer('Привет! Я помогу тебе не забыть о важных событиях:) \nПриступим?')
    await state.set_state(Register.name)
    await message.answer('Введите своё имя')


@router.message(Register.name)
async def nm(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите свой возраст')


@router.message(Register.age)
async def ag(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.fav_color)
    await message.answer('Введите свой любимый цвет')


@router.message(Register.fav_color)
async def fc(message: Message, state: FSMContext):
    await state.update_data(fav_color=message.text)
    data = await state.get_data()
    with open('data.txt', mode='w', encoding='utf8') as dt:
        dt.write(f'Имя: {data["name"]}, возраст: {data["age"]}, любимый цвет: {data["fav_color"]}.')
    await state.clear()


@router.message()
async def start_working(message: Message):
    await message.answer('Какое напоминание создать?')
