import requests

class APIClient:
    def __init__(self, api_url) -> None:
        self.api_url = api_url
    
    def fetch_data(self):
        response = requests.get(self.api_url)
        data = response.json()
        return data