# -*- coding: utf-8 -*-
# Sokoban_v0.4. Исчезновение кнопок '⬅' и '➡' при нажатии на них.

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
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton(u'⬅', callback_data='-1')
    itembtn2 = types.InlineKeyboardButton(u'➡', callback_data='+1')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Choose direction", reply_markup=markup)


# Handle pressing buttons
@bot.callback_query_handler(func=lambda call: True)
def echo_message(call):
    """
    On pressing button '⬅' adds the value '-1'.
    On pressing button '➡' adds the value '+1'.
    """
    bot.edit_message_text(
        call.data,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
        )


print("Program start")

bot.polling(none_stop=True)

print("Program finish")
