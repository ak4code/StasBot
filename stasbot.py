import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Пошел на хуй!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text + " Все равно пошел на хуй!")

bot.polling()