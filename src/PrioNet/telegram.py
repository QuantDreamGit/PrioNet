'''
Author: Giuseppe Priolo
Date: 2024-05-03
Description: This script is used to access the Telegram API key from the environment variable.

To run this script, you need to set the API_KEY environment variable with your Telegram API key.
You can set the environment variable using the export command in the terminal:
    - export API_KEY_TELEGRAM="your_telegram_api_key"
    - export CHAT_ID="your_telegram_chat_id"
'''
import os
import requests

class Telegram:
    def __init__(self, api_key=None, chat_id=None):
        # Check if the API keys are set
        if (api_key is None) and (chat_id is None):
            # Access the API key from the environment variable
            self.api_key = os.getenv("API_KEY_TELEGRAM")
            self.chat_id = os.getenv("CHAT_ID_TELEGRAM")
            # Check if the API keys are set
            if (self.api_key is None) or (self.chat_id is None):
                print("API key not found. Please set the API_clearKEY environment variable.")
                print("You can set the API key using the export command in the terminal:")
                print("export API_KEY_TELEGRAM='your_telegram_api_key'")
                print("export CHAT_ID='your_telegram_chat_id'")
                exit(1)
        else:
            self.api_key = api_key
            self.chat_id = chat_id

    def send_to_telegram(self, message):
        # Set the URL
        apiURL = f'https://api.telegram.org/bot{self.api_key}/sendMessage'
        # Send a message to the chat
        requests.post(apiURL, json={'chat_id': self.chat_id, 'text': message})

telegram = Telegram()
telegram.send_to_telegram("Hello from PrioNet!")