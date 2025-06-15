# set_webhook.py
import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
RAILWAY_URL = os.getenv("RAILWAY_URL")  # e.g., "https://dmrushbot.up.railway.app"
WEBHOOK_PATH = "/webhook"  # must match your FastAPI POST route

webhook_url = f"{RAILWAY_URL}{WEBHOOK_PATH}"
telegram_api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"

response = requests.post(telegram_api_url, json={"url": webhook_url})

print("Set webhook status:", response.status_code)
print("Response:", response.json())
