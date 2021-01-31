import os
import threading
import time
import schedule as schedule
import telebot
from dotenv import load_dotenv
from boobs import get_boobs
from weather import get_weather

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))
test = '-475951554'
vprotivogaze = '-447633079'


@bot.message_handler(commands=['start', ])
def send_welcome(message):
    print(message)
    bot.reply_to(message, f"Привет! {message.from_user.first_name} {message.from_user.last_name}")


@bot.message_handler(commands=['pogoda'])
def show_weather(message):
    bot.send_message(message.chat.id, get_weather())


@bot.message_handler(commands=['boobs'])
def show_boobs(message):
    bot.send_message(message.chat.id, get_boobs())


def day_weather():
    bot.send_message(vprotivogaze, get_weather())


def runBot():
    bot.polling()


def runSchedulers():
    schedule.every().day.at('09:00').do(day_weather)

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
