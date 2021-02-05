import os
import threading
import time
import schedule as schedule
import telebot
from dotenv import load_dotenv
from boobs import get_boobs
from weather import get_weather, get_forecast
from news import get_news

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode='HTML')
test = '-475951554'
vprotivogaze = '-447633079'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, мой кожаный друг! ")


@bot.message_handler(commands=['pogoda'])
def show_weather(message):
    bot.send_message(message.chat.id, get_weather())


@bot.message_handler(commands=['news'])
def show_news(message):
    bot.send_message(message.chat.id, get_news())


@bot.message_handler(commands=['boobs'])
def show_boobs(message):
    bot.send_message(message.chat.id, get_boobs())


def forecast():
    bot.send_message(vprotivogaze, get_forecast())


def news():
    bot.send_message(vprotivogaze, get_news())


def runBot():
    bot.polling()


def runSchedulers():
    schedule.every().day.at('21:00').do(forecast)
    schedule.every().day.at('10:00').do(news)
    schedule.every().day.at('13:00').do(news)
    schedule.every().day.at('18:00').do(news)

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
