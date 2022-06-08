# -*- coding: utf-8 -*-
# Sokoban_v1.0. Игра. Плюс перехват исключения IndexError.

import telebot

from telebot import types
from sokoban_config import token


bot = telebot.TeleBot(token)


def show_map(gmap):
    """
    Add buttons '⬆', '⬇', '⬅' and '➡'. Data output to chat.
    """
    gmap_width = str(gmap.find(u'॥\n') + 1)
    btn = types.InlineKeyboardButton
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        btn("", callback_data="0"),
        btn(u"⬆", callback_data="-" + gmap_width),
        btn(u"⬅", callback_data="-1"),
        btn(u"➡", callback_data="1"),
        btn("", callback_data="0"),
        btn(u"⬇", callback_data=gmap_width),
    )
    return {
        # 'text': gmap,
        'text': '<code>' + gmap + '</code>',   # object color and location
        # 'text': '<pre>' + gmap + '</pre>',   # object color and location
        'reply_markup': markup,
        'parse_mode': 'html'
    }


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def welcome_and_map(message):
    """
    Reply to user message '/start' or '/help'. Add map.
    """
    bot.send_message(message.chat.id,
    "Hi, {0.first_name}!\n"
    "I am <b>{1.first_name}</b>.\n".format(
        message.from_user, bot.get_me()), parse_mode='html')

    # Game Map
    gmap = u"""
        ॥॥॥॥॥॥॥॥॥॥
        ॥॥॥॥॥  . ॥
        ॥  ●☿● ● ॥
        ॥     ..॥॥
        ॥॥॥॥॥॥॥॥॥॥
    """.replace('\n        ', '\n')

    # Message
    bot.send_message(message.chat.id, **show_map(gmap))


def replace_on_map(game_map, pos, char):
    """
    Function makes replacements on the map.
    """
    return game_map[:pos] + char + game_map[pos + 1:]


# Handle pressing buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """
    Hero and container movements.
    """
    try:
        if call.message:
            gmap = call.message.text
            movement = int(call.data)

            pos = gmap.find(u'☿')
            if pos < 0:
                pos = gmap.find(u'♆')

            new_pos = pos + movement
            new_place = gmap[new_pos]
            next_place = gmap[new_pos + movement]

            if new_place in (' ', '.') or (new_place in (u'●', u'◉') and next_place in (' ', '.')):
                if new_place in (u'●', u'◉'):
                    gmap = replace_on_map(gmap, new_pos + movement, u'◉' if next_place == '.' else u'●')
                gmap = replace_on_map(gmap, pos, ' ' if gmap[pos] == u'☿' else '.')
                gmap = replace_on_map(gmap, new_pos, u'☿' if new_place in (' ', u'●') else u'♆')

            if gmap != call.message.text:
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    **show_map(gmap)
                )
    except IndexError as IE:
        print(repr(IE))


print("Program start")

bot.polling(none_stop=True)

print("Program finish")
