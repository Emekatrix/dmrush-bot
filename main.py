from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Set in Railway Environment Variables
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Define a basic command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to DMRushBot!")

# Webhook route
@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

# Set webhook when the server starts
@app.before_first_request
def set_webhook():
    webhook_url = os.getenv("WEBHOOK_URL")  # Set this in Railway as well
    bot.remove_webhook()
    bot.set_webhook(url=f"{webhook_url}/{TOKEN}")

# Default route
@app.route('/')
def index():
    return "DMRushBot is running."

if __name__ == "__main__":
    app.run(debug=False, port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')
