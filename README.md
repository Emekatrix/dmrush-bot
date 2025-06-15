# 🤖 DMRushBot

DMRushBot is a Telegram bot that connects **buyers** and **sellers** using a unique coin-based interaction model. Buyers post items they want to purchase, and sellers send DM Coins to get access to pitch their offer directly in the buyer’s DMs.

Built with:
- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- [SQLite](https://www.sqlite.org/)
- [Google Sheets](https://www.google.com/sheets/about/) (for logging/analytics)
- Hosted on [Railway](https://railway.app/)
- Deployed via [GitHub Webhooks](https://docs.github.com/en/webhooks)

---

## 🛠 Features

- 💬 Coin-based direct messaging (DM) between buyers and sellers
- ⏱️ Optional 5-minute DM countdown for offers
- 💰 Seller wallet with Coin balance and limits
- 🔁 Coin refund logic if no purchase happens
- 🔐 Rate limiting and abuse protection
- 👤 Admin commands for banning/resetting users
- 📊 Logs all Coin transactions to Google Sheets
- 🌐 Webhook-ready deployment via Railway

---

## 📦 Setup & Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/DMRushBot.git
cd DMRushBot

2. Set Your Environment Variables
In Railway or locally, configure the following:
BOT_TOKEN – Your Telegram bot token from @BotFather
GOOGLE_SERVICE_ACCOUNT – JSON string of your Google Sheets service account
SHEET_ID – Google Sheet ID for logging
ADMIN_IDS – Comma-separated Telegram user IDs of admins
You can place these in .env for local development:
BOT_TOKEN=123456:ABC-your-telegram-token
GOOGLE_SERVICE_ACCOUNT={...}
SHEET_ID=your_google_sheet_id
ADMIN_IDS=12345678,987654321

3. Deploy on Railway
Push the repo to GitHub
Go to Railway
Click "New Project" > "Deploy from GitHub Repo"
Add environment variables in Railway Dashboard
Click Deploy

🧩 Commands
Command         Description
/start          Register user and create wallet
/postitem       Buyer posts item to buy
/sendcoin       Seller sends Coin to buyer
/acceptcoin     Buyer accepts a seller's Coin offer
/wallet         View wallet balance and transactions
/refunds        Manual refund check (admin only)
/banuser        Ban abusive user (admin only)
/resetwallet    Reset a user’s wallet (admin only)


📄 License
This project is licensed under the MIT License.

👤 Author
Emeka Nzeribe
DMRushBot Creator
📧 sir.emekanzeribe@gmail.com
