api_id = 23313724
api_hash = "9a048695d31d76ed4d977920a8b40eec"

from telethon.sync import TelegramClient, events
import os
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl import types

# Initialize the Telegram client
with TelegramClient('name', api_id, api_hash) as client:
    # Get the chat object
    title = 'Project Notes'
    chat = client.get_entity(title)

    # Look for the desired file in the chat
    file_name = 'CUSAT-EXAM.PDF'
    found_file = None
    for message in client.iter_messages(chat):
        if message.media and isinstance(message.media, types.Document):
            if message.media.document.file_name == file_name:
                found_file = message.media.document
            break


    if found_file:
        # Download the file and save it to a variable
        file_path = os.path.join(os.getcwd(), file_name)
        client.download_media(found_file, file_path)

        with open(file_path, 'rb') as f:
            Final_file = f.read()

        # Delete the downloaded file
        os.remove(file_path)

        print(f"File '{file_name}' found and contents saved to variable 'Final_file'")
    else:
        print(f"File '{file_name}' not found in '{title}' chat")