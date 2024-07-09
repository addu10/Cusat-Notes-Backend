# app.py

import os
from telethon.sync import TelegramClient
import pickle
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_no = os.getenv("phone")


with open('telegram_credentials.txt', 'rb') as f:
    session_name = pickle.load(f)

client = TelegramClient('name', api_id, api_hash)