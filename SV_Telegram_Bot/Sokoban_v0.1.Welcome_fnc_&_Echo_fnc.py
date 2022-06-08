# -*- coding: utf-8 -*-
# Sokoban_v0.1. Функция приветствия и эхо-функция.

import telebot

from telebot import types
from sokoban_config import token


bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Reply to user message '/start' or '/help'.
    """
    bot.send_message(message.chat.id,
    "Hi, {0.first_name}!\n"
    "I am <b>{1.first_name}</b>.\n"
    "I am here to echo your kind words back to you.\n"
    "Just say anything nice and I'll say the exact same thing to you!".format(
        message.from_user, bot.get_me()), parse_mode="html")


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
