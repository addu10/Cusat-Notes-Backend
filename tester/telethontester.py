api_id = 23313724
api_hash = "9a048695d31d76ed4d977920a8b40eec"

from telethon.sync import TelegramClient, events
import os
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from tqdm import tqdm

found_file = None

with TelegramClient('name', api_id,api_hash ) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer='username',
        limit=500,
        hash=0,
    ))
    
    title= 'Project Notes'
    for chat in result.chats:
        print(chat)

        """if chat.title == title:
            messages = client.get_messages(chat,limit=200)

            for message in tqdm(messages):
                message.download_media('./'+title+'/')
                """

    
