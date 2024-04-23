from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import time
import schedule

import keyboards as kbs

router = Router()


class Reminds(StatesGroup):
    remind1 = State()
    remind2 = State()


class Register(StatesGroup):
    name = State()
    age = State()
    fav_color = State()


def send_message(message):
    bot.send_message(message.chat.id, 'fsgdhdfs')


@router.message(CommandStart())
async def cmnd_strt(message: Message, state: FSMContext):
    await message.answer('Привет! Я помогу вам не забыть о важных событиях:) \nПриступим?')
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
        dt.write(f'Имя: {data["name"]}; Возраст: {data["age"]}; Любимый цвет: {data["fav_color"]}.')
        dt.close()
    await state.clear()
    await state.set_state(Reminds.remind1)
    await message.answer('Какое напоминание создать?')


@router.message(Reminds.remind1)
async def set_remind(message: Message, state: FSMContext):
    await state.update_data(remind1=message.text)
    data = await state.get_data()
    with open('data.txt', mode='a', encoding='utf8') as dt:
        dt.write(f'\n{data["remind1"]}')
        dt.close()
    await message.answer('Времени осталось:', reply_markup=kbs.time)
    await state.clear()


@router.message(F.text == '15 минут')
async def set_remind(message: Message, state: FSMContext):
    await message.answer('Заметка успешно создана! Напоминание произойдет через 15 минут')
    await state.set_state(Reminds.remind1)
    await message.answer('Какое напоминание создать?')


@router.message(F.text == '1 час')
async def set_remind(message: Message, state: FSMContext):
    await message.answer('Заметка успешно создана! Напоминание произойдет через 1 час')
    await state.set_state(Reminds.remind1)
    await message.answer('Какое напоминание создать?')


@router.message(F.text == '1 день')
async def set_remind(message: Message, state: FSMContext):
    await message.answer('Заметка успешно создана! Напоминание произойдет через 1 день')
    await state.set_state(Reminds.remind1)
    await message.answer('Какое напоминание создать?')


@router.message(F.text == '1 неделя')
async def set_remind(message: Message, state: FSMContext):
    await message.answer('Заметка успешно создана! Напоминание произойдет через 1 неделю')
    await state.set_state(Reminds.remind1)
    await message.answer('Какое напоминание создать?')


