# dmrush-bot

DMRushBot is a Telegram bot that powers buyer-driven commerce using a unique Coin incentive system.

### 🔥 Key Features

- 💬 Buyers post what they want to purchase
- 🪙 Sellers send DM Coins to get 5-minute DM access
- 💸 Buyers earn Coins and can cash out after a successful purchase
- ⏳ 5-minute DM countdown logic per seller
- 🔁 Automatic refunds if buyer doesn’t purchase
- ⚙️ Admin commands: /banuser, /resetwallet, etc.

---

### 🚀 Technologies

- **Telegram Bot** via [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- **Database:** SQLite
- **Backend:** Python + Flask
- **Bot Hosting:** [Railway](https://railway.app/)
- **Google Sheets** (optional): As backend dashboard or storage

---

### 📦 Project Structure

DMRushBot/
├── .env.example                # Example env vars (for dev or Railway)
├── .gitignore                 # Files to ignore in Git
├── LICENSE                    # MIT License
├── README.md                  # Project overview
├── bot.py                     # Main Telegram bot logic
├── database/
│   └── db.sqlite              # SQLite database (runtime, auto-generated)
├── handlers/
│   ├── buyer.py               # Buyer-related commands (e.g. /postitem)
│   ├── seller.py              # Seller actions (e.g. /sendcoin)
│   └── admin.py               # Admin-only commands (/banuser, /resetwallet)
├── models/
│   ├── user.py                # DB model logic for users
│   ├── wallet.py              # DB logic for coin handling
│   └── transaction.py         # Logs and refunds
├── services/
│   ├── google_sheets.py       # Append logs to Google Sheets
│   └── scheduler.py           # Refund timer logic (manual or cron)
├── utils/
│   ├── auth.py                # Authentication & permission utils
│   ├── logger.py              # Logging for dev/debug
│   └── constants.py           # Global constants & configs
├── .railway/
│   └── project.json           # Railway bootstrapping
└── requirements.txt           # Python package dependencies
---

### ⚙️ Environment Variables

Create a `.env` file with the following:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
GOOGLE_SHEET_ID=optional_google_sheet_id


🛠️ Deployment (Railway)
Create a Railway account
Link this GitHub repo
Add your .env variables
Deploy the bot 🚀

📖 Admin Commands
/banuser <@username> – Ban abusive users
/resetwallet <@username> – Reset user's wallet
/refundcoins – Trigger refund manually

👨‍🔧 Author
Emeka Nzeribe
Telegram: @DMRushBot
License: MIT

🤝 Contribute
Pull requests welcome. For major changes, please open an issue first.
