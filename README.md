# Bot Telegram Flasha
A Telegram bot built with Python and Aiogram to automate admin-controlled bot interactions and basic data handling.
<img width="2269" height="677" alt="image" src="https://github.com/user-attachments/assets/fd887573-3129-45e8-84d6-0cc361699bf3" />

## Overview
This project is a Telegram bot developed using Python and Aiogram.  
It is designed to provide a structured bot architecture with configuration management, admin-only actions, routing, and local database support.

## Goal
The goal of this project is to build a clean and extensible Telegram bot that can be used as a base for automation, admin commands, and future feature expansion.

## Features
- Built with Python and Aiogram
- Environment-based configuration using `.env`
- Admin-only middleware support
- Modular project structure
- SQLite database support
- Easy to extend with new routes and handlers

## Project Structure
```text
app/
├── middlewares/
├── routers/
├── ui/
├── config.py
├── logging_config.py
└── main.py
requirements.txt
.gitignore


### 8) التقنيات
```md
## Tech Stack
- Python 3.12
- Aiogram
- SQLite
- python-dotenv

## Setup and Run

### 1. Clone the repository
```bash
git clone https://github.com/DevEmad2001/bot-telegram-flasha.git
cd bot-telegram-flasha

2. Create virtual environment
python -m venv .venv

3. Activate virtual environment

.venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Create .env file

BOT_TOKEN=your_bot_token
ADMIN_IDS=your_admin_id
DB_PATH=bot.db

6. Run the bot
python -m app.main


### 10) ملاحظات الأمان
```md
## Security Notes
- Never upload your `.env` file
- Never expose your Telegram bot token
- Regenerate the token if it was ever shared publicly
