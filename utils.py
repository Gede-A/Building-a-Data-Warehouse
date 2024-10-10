# utils.py
import logging

def setup_logger():
    logging.basicConfig(
        filename='logs/scraper.log', 
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def log_message(message):
    logging.info(message)

def log_error(error):
    logging.error(error)
