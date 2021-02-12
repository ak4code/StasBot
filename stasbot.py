import os
import threading
import time
import schedule as schedule
import telebot
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from boobs import get_boobs
from weather import get_weather, get_forecast
from news import get_news

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode='HTML')
test = '-475951554'
vprotivogaze = '-447633079'


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Погода", callback_data="weather"),
               InlineKeyboardButton("Новость", callback_data="news"),
               InlineKeyboardButton("Сиськи", callback_data="boobs"))
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, что хотел?", reply_markup=gen_markup())


@bot.message_handler(regexp="^стас?")
def directly_ask(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, что хотел?", reply_markup=gen_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "weather":
        bot.send_message(call.message.chat.id, get_weather())
    elif call.data == "news":
        bot.send_message(call.message.chat.id, get_news())
    elif call.data == "boobs":
        bot.send_message(call.message.chat.id, get_boobs())


def forecast():
    bot.send_message(vprotivogaze, get_forecast())


def news():
    bot.send_message(vprotivogaze, get_news())


def boobs():
    bot.send_message(vprotivogaze, f"А вот и пятничные сиськи!")
    bot.send_message(vprotivogaze, get_boobs())


def runBot():
    bot.polling(True)


def runSchedulers():
    schedule.every().friday.at('16:00').do(boobs)
    schedule.every().days.at('21:00').do(forecast)
    schedule.every().days.at('10:00').do(news)
    schedule.every().days.at('13:00').do(news)
    schedule.every().days.at('19:30').do(news)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runSchedulers)
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
