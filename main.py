from telebot import *

bot = telebot.TeleBot('7130979300:AAHLzOh5RIzqLS7SZJr_nQXMr1VvOHu7Yx0')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("какая-то инфа")
    item2 = types.KeyboardButton("еще какая-то инфа")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nкакая-то инфа — для получения инфы\nеще какая-то инфа — для получения еще какой-то инфы ',
                     reply_markup=markup)


bot.polling(none_stop=True, interval=0)
