api_id = 23313724
api_hash = "9a048695d31d76ed4d977920a8b40eec"

from telethon import TelegramClient, events, sync
import os, asyncio


# Create a new event loop
loop = asyncio.new_event_loop()

# Create the Telegram client with the new event loop
client = TelegramClient('me', api_id, api_hash, loop=loop)

# Connect to the Telegram server
loop.run_until_complete(client.start())

# Define the chat to access (replace 'CUSAT NOTES' with the actual name or ID of the chat)
chat = client.get_entity('Adnan_UAE')

# Ask the user which file to download
filename = input('Enter the filename of the file you want to download: ')

# Define an asynchronous function to iterate over the messages in the chat
async def download_file():
    async for message in client.iter_messages(chat):
        for file in message.media:
            if file.name == filename:
                # Download the file to the "C:\Downloads" directory
                file_path = os.path.join('C:\\Downloads', filename)
                await client.download_media(file, file_path)
                print(f'Downloaded file {filename} to {file_path}')
                return

# Run the asynchronous function in the event loop
loop.run_until_complete(download_file())

# Disconnect from the Telegram server
loop.run_until_complete(client.disconnect())

# Close the event loop
loop.close()