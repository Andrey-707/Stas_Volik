# -*- coding: utf-8 -*-
# Sokoban_v0.2. Первые кнопки '⬅' и '➡'.

import telebot

from telebot import types
from sokoban_config import token


bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    """
    Reply to user message '/start' or '/help'. Add buttons '⬅' and '➡'.
    """
    bot.send_message(message.chat.id,
    "Hi, {0.first_name}!\n"
    "I am <b>{1.first_name}</b>.\n".format(
        message.from_user, bot.get_me()), parse_mode='html')

    # Buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton(u'⬅')
    itembtn2 = types.KeyboardButton(u'➡')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Choose direction", reply_markup=markup)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    """
    Echo function.
    """
    bot.reply_to(message, message.text)


print("Program start")

bot.polling(none_stop=True)

print("Program finish")
