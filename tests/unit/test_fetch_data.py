import unittest
from unittest.mock import Mock, patch

import requests

from src.APIClient import APIClient


class APIClientTests(unittest.TestCase):
    def test_fetch_data_success(self):
        api_url = "http://example.com/api"
        expected_data = {"slip": {"slip_id": "2", "advice": "Example advice."}}
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = expected_data

        with patch("src.APIClient.requests.get", return_value=response_mock):
            client = APIClient(api_url)
            data = client.fetch_data()
            self.assertEqual(data, expected_data)

    def test_fetch_data_failure(self):
        api_url = "http://example.com/api"
        response_mock = Mock()
        response_mock.status_code = 404
        response_mock.raise_for_status.side_effect = requests.HTTPError("Not Found")

        with patch("src.APIClient.requests.get", return_value=response_mock):
            client = APIClient(api_url)

            with self.assertRaises(requests.HTTPError):
                client.fetch_data()
