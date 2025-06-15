import telebot
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
RAILWAY_URL = os.environ['RAILWAY_PUBLIC_DOMAIN']  # e.g., https://dmrushbot.up.railway.app

bot = telebot.TeleBot(BOT_TOKEN)

webhook_url = f"{RAILWAY_PUBLIC_DOMAIN}/webhook"
bot.remove_webhook()
success = bot.set_webhook(url=webhook_url)

print("Webhook set:", success)
