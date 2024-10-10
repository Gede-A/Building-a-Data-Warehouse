# scraper.py
from telethon.sync import TelegramClient
import pandas as pd
import config

# Initialize Telegram client
client = TelegramClient('session', config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)

def scrape_messages(channel_username, limit=100):
    client.start(phone=config.PHONE_NUMBER)
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
    for channel in config.CHANNEL_USERNAMES:
        print(f"Scraping {channel}")
        df = scrape_messages(channel)
        df.to_csv(f"data/raw/{channel}.csv", index=False)
        print(f"Saved {channel}.csv")
