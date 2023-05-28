import requests
import os
import logging

class APIClient:
    def __init__(self, api_url) -> None:
        self.api_url = api_url
        self.api_key = os.environ.get('API_KEY')
    
    def fetch_data(self):
        response = requests.get(self.api_url)
        logging.info('Data download successful.')
        data = response.json()
        return data