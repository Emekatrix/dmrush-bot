from telebot import TeleBot, types
import os
import json
import sqlite3
from flask import Flask, request

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

BOT_TOKEN = config["BOT_TOKEN"]
bot = TeleBot(BOT_TOKEN)
app = Flask(__name__)

# SQLite setup
conn = sqlite3.connect("db.sqlite", check_same_thread=False)
cursor = conn.cursor()

# Ensure tables exist
cursor.execute("""CREATE TABLE IF NOT EXISTS wallets (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance INTEGER DEFAULT 0
)""")
conn.commit()

# Start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    cursor.execute("INSERT OR IGNORE INTO wallets (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    bot.send_message(message.chat.id, f"Welcome to DMRushBot, {username}!")

# Coin sending logic (example)
@bot.message_handler(commands=['sendcoin'])
def handle_sendcoin(message):
    bot.reply_to(message, "Feature coming soon!")

# Flask webhook handler
@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 'OK', 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
