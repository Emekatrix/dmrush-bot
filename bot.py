import telebot
import os

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to DMRushBot! 🚀")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")
