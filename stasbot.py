import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    listen(message)
    bot.reply_to(message, f"Привет! {message.from_user.first_name} {message.from_user.last_name}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    listen(message)
    bot.reply_to(message, message.text + "")


def listen(m):
    print(m)

bot.polling(none_stop=True)