from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

strt = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/start')]],
                           resize_keyboard=True)

time = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='15 минут'),
                                      KeyboardButton(text='1 час')],
                                     [KeyboardButton(text='1 день'),
                                      KeyboardButton(text='1 неделя')]],
                           resize_keyboard=True)
# кнопки для выбора времени напоминания
