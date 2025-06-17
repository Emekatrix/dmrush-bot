# 🤖 DMRushBot

DMRushBot is a Telegram bot that connects buyers and sellers using a coin-based DM economy.  
It’s built with **python-telegram-bot v21** (async), served by FastAPI, and stores data in PostgreSQL via Tortoise ORM.  
The project is designed for one-click deployment on Railway with a production-grade webhook.

---

## ✨ Features

Bot UX                      
- `/start` greets and creates a wallet 
- Echo handler for quick testing 
- Easily extend with new commands & inline keyboards

Architecture  
- `python-telegram-bot` async core 
- FastAPI receives webhooks 
- PostgreSQL via Railway plugin 
- Tortoise ORM models & migrations

Dev Experience 
- Hot-reload locally with Uvicorn 
- `.env` config 
- Typed models 
- Clean repo structure

Deployment 
- 100 % Railway-ready (Procfile, requirements) 
- One-time `run_once.py` to set webhook 
- Automatic DB schema generation |

---

## 🗂 Project Structure

```text DMRushBot/
├── bot/                     # All bot-related logic
│   ├── __init__.py
│   ├── handlers.py          # Telegram command/message handlers
│   └── models.py            # Tortoise ORM models (User, Message)
│
├── .env.example             # Example .env (for development)
├── main.py                  # FastAPI app and webhook setup
├── requirements.txt         # All dependencies
├── Procfile                 # For Railway deployment
├── runtime.txt              # Optional (used by some platforms)
├── README.md                # Setup & usage instructions```

---

## 🚀 Quick Start (Local)

bash
# 1. Clone
git clone https://github.com/YOUR-ORG/DMRushBot.git && cd DMRushBot

# 2. Create venv
python -m venv .venv && source .venv/bin/activate

# 3. Install deps
pip install -r requirements.txt

# 4. Copy env template
cp .env.example .env
# ➡️ Fill TELEGRAM_API_TOKEN, RAILWAY_URL (e.g. http://localhost:8000), DATABASE_URL

# 5. Launch dev server
uvicorn main:app --reload

---
Navigate to http://localhost:8000/api/docs for automatic Swagger docs.


🛠 Environment Variables

Key: TELEGRAM_API_TOKEN
Purpose: Bot token from @BotFather
Example: 123456:ABC...

Key: RAILWAY_URL
Purpose: Public base URL (Railway gives you this)
Example: https://dmrushbot.up.railway.app

Key: DATABASE_URL
Purpose: PostgreSQL URI (Railway plugin auto-creates)
Example: postgresql://user:pass@host:5432/db


🐘 Database Models (Tortoise)
class            User(models.Model):
 id           =   fields.IntField(pk=True)
 telegram_id  =   fields.BigIntField(unique=True)
 username     =   fields.CharField(255, null=True)
 first_name   =   fields.CharField(255, null=True)
 last_name    =   fields.CharField(255, null=True)

class            Message(models.Model):
 id           =   fields.IntField(pk=True)
 user         =   fields.ForeignKeyField("models.User", related_name="messages")
 text         =   fields.TextField()
 timestamp    =   fields.DatetimeField(auto_now_add=True)

On startup, generate_schemas=True auto-creates the tables.


☁️ Deploy on Railway (Production)

1. Fork / push this repo to GitHub.

2. Create new project → “Deploy from GitHub repo”.

3. Add PostgreSQL plugin (DATABASE_URL appears automatically).

4. Add variables → TELEGRAM_API_TOKEN and RAILWAY_URL (your Railway domain).

5. Railway builds & starts via the Procfile:
   web: uvicorn main:app --host 0.0.0.0 --port $PORT

6. Open the Railway Shell and run:
   python run_once.py   # sets Telegram webhook exactly once

7. Send /start to your bot 🎉



🔧 Extending the Bot

Task: New command
Where?: bot/handlers.py
Hint: Add CommandHandler

Task: DM-coin logic
Where?: new file in bot/
Hint: Import models, update DB

Task: Migrations
Where?: tortoise-orm CLI
Hint: Or rely on generate_schemas

Task: Tests
Where?: tests/ dir
Hint: Use pytest + asyncio



⚖️ License
MIT © 2025 Emeka Nzeribe DMRushBot Creator
📧 sir.emekanzeribe@gmail.com
