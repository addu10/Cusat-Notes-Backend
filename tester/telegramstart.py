# auth_telegram.py

import os
from telethon.sync import TelegramClient
from dotenv import find_dotenv, load_dotenv
import pickle

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_no = os.getenv("phone")

client = TelegramClient('name', api_id, api_hash)

client.start()
print("Enter the code sent to your phone:")
code = input()
client.sign_in(phone_no, code)

# Store the authentication credentials securely
with open('telegram_credentials.txt', 'wb') as f:
    pickle.dump(client.session.save(),f)