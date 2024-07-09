api_id = 23313724
api_hash = "9a048695d31d76ed4d977920a8b40eec"

from telethon.sync import TelegramClient, events
import os
from telethon.tl.functions.messages import GetDialogsRequest
from tqdm import tqdm

title = 'Project Notes'
file_to_download = input("Enter the file name: ")
found_file = None

with TelegramClient('name', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer='username',
        limit=500,
        hash=0,
    ))
    
    
    for chat in result.chats:

        if chat.title == title:
            messages = client.get_messages(chat, limit=200)

            for message in tqdm(messages):
                # Check if the message contains the desired file
                if message.media and hasattr(message.media, 'document') and message.media.document.mime_type == 'application/pdf' and message.media.document.attributes[0].file_name == file_to_download:
                    message.download_media('./' + title + '/')
                    found_file = "success"
                
                if found_file == "success":
                    file_path = os.path.join(os.getcwd(), title,file_to_download)
                    
                    print(f"File '{file_to_download}' found and contents saved")
                        
                    
                else:
                    print(f"File '{file_to_download}' not found in '{title}' chat")
        if(found_file=="success"):
            break


            