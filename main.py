import os
import telebot
from telebot import types
from web3 import Web3
import time as t
import requests
import settings
import dbconnect



def main():
    API_KEY = settings.telegram_api_key
    bot = telebot.TeleBot(API_KEY)

    @bot.message_handler(commands=["start"])
    def start(message):
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        first_item = types.KeyboardButton('Balance')
        second_item = types.KeyboardButton('Transfer')
        thrity_item = types.KeyboardButton('Referral')
        markup.add(first_item, second_item, thrity_item)

        bot.send_message(message.chat.id, "Hello, "+ message.from_user.username +". SferocoinBot is a Bot for widthraw/transfer coins\nChoose Method", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def handleText(message):
        if message.text == "Balance":
            balance = dbconnect.get_balance(message.from_user.id)
            bot.send_message(message.chat.id, "Your Balance Is: " + str(balance))







    bot.polling(none_stop=True)


# Press the green button in the gutter to run the script.

main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
