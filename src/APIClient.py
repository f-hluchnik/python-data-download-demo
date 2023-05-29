import logging

import requests


class APIClient:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def fetch_data(self) -> dict:
        response = requests.get(self.api_url, timeout=3)

        if response.status_code == requests.codes.ok:
            logging.info("Data download successful.")
            return response.json()
        logging.error(
            "Failed to fetch the data. Status code: %d", response.status_code
        )
        response.raise_for_status()
