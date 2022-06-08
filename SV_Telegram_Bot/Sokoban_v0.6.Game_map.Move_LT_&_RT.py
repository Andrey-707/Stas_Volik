# -*- coding: utf-8 -*-
# Sokoban_v0.6. Карта игры Движение влево ('⬅') и вправо ('➡').

import telebot

from telebot import types
from sokoban_config import token


bot = telebot.TeleBot(token)


def show_msg(msg):
    """
    Add buttons '⬅' and '➡'. Data output to chat.
    """
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton(u'⬅', callback_data='-1')
    itembtn2 = types.InlineKeyboardButton(u'➡', callback_data='+1')
    markup.add(itembtn1, itembtn2)
    return {
        'text': msg,
        # 'text': '<code>' + msg + '</code>',   # object color and location
        # 'text': '<pre>' + msg + '</pre>',     # object color and location
        'reply_markup': markup,
        'parse_mode': 'html'
    }


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    """
    Reply to user message '/start' or '/help'. Add map.
    """
    bot.send_message(message.chat.id,
    "Hi, {0.first_name}!\n"
    "I am <b>{1.first_name}</b>.\n".format(
        message.from_user, bot.get_me()), parse_mode='html')

    # Game Map
    gmap = u"""
        ██████████
        ██████ . █
        █  ◯☿◯ ◯ █
        █     ..██
        ██████████
    """.replace('\n        ', '\n')

    # Message
    bot.send_message(message.chat.id, **show_msg(gmap))


# Handle pressing buttons
@bot.callback_query_handler(func=lambda call: True)
def echo_message(call):
    """
    On pressing button '⬅' adds the value '-1'.
    On pressing button '➡' adds the value '+1'.
    """
    gmap = call.message.text
    movement = int(call.data)
    pos = gmap.find(u'☿')
    gmap = gmap[:pos] + ' ' + gmap[pos+1:]
    pos += movement    
    gmap = gmap[:pos] + u'☿' + gmap[pos+1:]
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        **show_msg(gmap)
        )


print("Program start")

bot.polling(none_stop=True)

print("Program finish")
