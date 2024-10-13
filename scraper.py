# # scraper.py
# from telethon.sync import TelegramClient
# import pandas as pd
# from config import setting

# # Initialize Telegram client
# client = TelegramClient('session', setting.TELEGRAM_API_ID, setting.TELEGRAM_API_HASH)

# def scrape_messages(channel_username, limit=5000):
#     client.start(phone=setting.PHONE_NUMBER)
#     messages = client.get_messages(channel_username, limit=limit)
    
#     data = []
#     for message in messages:
#         data.append({
#             'Message ID': message.id,
#             'Sender': message.sender_id,
#             'Date': message.date,
#             'Message': message.message
#         })
    
#     df = pd.DataFrame(data)
#     return df

# def scrape_channels():
#     for channel in setting.CHANNEL_USERNAMES:
#         print(f"Scraping {channel}")
#         df = scrape_messages(channel)
#         df.to_csv(f"data/raw/scraped.csv", index=False)
#         print(f"Saved {channel}.csv")



# def scrape_media(channel_username, limit=5000):
#     client.start(phone=setting.PHONE_NUMBER)
#     messages = client.get_messages(channel_username, limit=limit)
    
#     data = []
#     media_path = f"data/media/images"
#     for message in messages:
#         if message.media:
#             file_path = client.download_media(message, file=media_path) 
#     df = pd.DataFrame(data)
#     return df

# def scrape_channel():
#     for channel in setting.CHANNEL_USERNAME:
#         print(f"Scraping {channel}")
#         df = scrape_media(channel)
#         df.to_csv(f"data/media", index=False)
#         # print(f"Saved {channel}.csv")


# if __name__ == "__main__":
#     scrape_channels()
#     scrape_channel()


# scraper.py
import os
from telethon.sync import TelegramClient
import pandas as pd
from config import setting

# Initialize Telegram client
client = TelegramClient('session', setting.TELEGRAM_API_ID, setting.TELEGRAM_API_HASH)

def scrape_messages(channel_username, limit=5000):
    client.start(phone=setting.PHONE_NUMBER)
    messages = client.get_messages(channel_username, limit=limit)
    
    data = []
    for message in messages:
        data.append({
            'Message ID': message.id,
            'Sender': message.sender_id,
            'Date': message.date,
            'Message': message.message
        })
    
    df = pd.DataFrame(data)
    return df

def scrape_channels():
    for channel in setting.CHANNEL_USERNAMES:
        print(f"Scraping {channel}")
        # Ensure directories exist
        os.makedirs("data/raw", exist_ok=True)
        
        # Scrape messages and save to CSV
        df = scrape_messages(channel)
        df.to_csv(f"data/raw/scraped.csv", index=False)
        print(f"Saved {channel}.csv")

def scrape_media(channel_username, limit=5000):
    client.start(phone=setting.PHONE_NUMBER)
    messages = client.get_messages(channel_username, limit=limit)
    
    media_path = f"data/media/images"
    os.makedirs(media_path, exist_ok=True)  # Ensure media directory exists
    
    data = []
    for message in messages:
        if message.media:
            file_path = client.download_media(message, file=media_path) 
            if file_path:
                data.append({
                    'Message ID': message.id,
                    'Sender': message.sender_id,
                    'Date': message.date,
                    'Media Path': file_path
                })

    df = pd.DataFrame(data)
    return df

def scrape_media_channels():
    for channel in setting.CHANNEL_USERNAMES:
        print(f"Scraping media from {channel}")
        df = scrape_media(channel)
        
        # Save media data to a CSV file
        media_csv_path = f"data/media/{channel.split('/')[-1]}_media.csv"
        df.to_csv(media_csv_path, index=False)
        print(f"Saved media for {channel} to {media_csv_path}")

if __name__ == "__main__":
    scrape_channels()  
    scrape_media_channels() 
