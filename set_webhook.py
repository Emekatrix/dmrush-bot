import telebot
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
RAILWAY_URL = os.environ['web-production-10e05.up.railway.app']  # e.g., https://dmrushbot.up.railway.app

bot = telebot.TeleBot(BOT_TOKEN)

webhook_url = f"{RAILWAY_URL}/webhook"
success = bot.remove_webhook()
success = bot.set_webhook(url=webhook_url)

print("Webhook set:", success)
