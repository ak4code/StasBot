import os
import threading
import time
import schedule as schedule
import telebot
from dotenv import load_dotenv
import requests

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))
test = '-475951554'
vprotivogaze = '-447633079'


@bot.message_handler(commands=['start',])
def send_welcome(message):
    print(message)
    bot.reply_to(message, f"Привет! {message.from_user.first_name} {message.from_user.last_name}")


@bot.message_handler(commands=['pogoda'])
def show_weather(message):
    url = f'https://api.openweathermap.org/data/2.5/group?id=542420,483661,484670&appid={os.getenv("W_API_KEY")}&lang=ru&units=metric'
    r = requests.get(url=url)
    weathers = r.json().get('list')
    for weather in weathers:
        bot.send_message(message.chat.id,
                         f'{weather.get("name")} {weather.get("weather")[0].get("description")} температура {weather.get("main").get("temp")} °C')


def day_weather():
    url = f'https://api.openweathermap.org/data/2.5/group?id=542420,483661,484670&appid={os.getenv("W_API_KEY")}&lang=ru&units=metric'
    r = requests.get(url=url)
    weathers = r.json().get('list')
    for weather in weathers:
        bot.send_message(vprotivogaze,
                         f'{weather.get("name")} {weather.get("weather")[0].get("description")} температура {weather.get("main").get("temp")} °C')


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
