# Building-a-Data-Warehouse
Building a Data Warehouse to store data on Ethiopian medical business data scraped from telegram channels.

# Telegram Data Scraping Pipeline

## Setup

1. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Set up your Telegram API credentials in `config.py`.

3. Run the scraper:
    ```
    python scraper.py
    ```

4. Preprocess the data:
    ```
    python preprocess.py
    ```

5. Store the data into a database:
    ```
    python storage.py
    ```

6. Automate the process using the scheduler:
    ```
    python scheduler.py
    ```

## Logs
Logs are stored in the `logs/` directory.

