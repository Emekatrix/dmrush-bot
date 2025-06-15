from fastapi import FastAPI, Request
import telebot
from bot import bot

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    body = await request.body()
    update = telebot.types.Update.de_json(body.decode("utf-8"))
    bot.process_new_updates([update])
    return {"status": "ok"}
