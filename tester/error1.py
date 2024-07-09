"""async with TelegramClient('name', api_id, api_hash) as client:
        print("Inside telegram")
        result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer='Project Notes',
        limit=10000,
        hash=0,
    ))
    
    print(result.chats)
    
    print("Outside telegram")
    for chat in result.chats:
        print(chat)
        print("Inside chat")
        if chat.title == title:
            print("title matched")
            messages = client.get_messages(chat, limit=200)

            for message in tqdm(messages):
                print("Inside messages")
                # Check if the message contains the desired file
                if message.media and hasattr(message.media, 'document') and message.media.document.mime_type == 'application/pdf' and message.media.document.attributes[0].file_name == file_to_download:
                    message.download_media('./' + title + '/')
                    found_file = "success"
                    print(f"File '{file_to_download}' found and contents saved")
                  
                else:
                    print(f"File '{file_to_download}' not found in '{title}' chat")
        if(found_file=="success"):
            return "success"
        else:
            return "fail"
            """
    