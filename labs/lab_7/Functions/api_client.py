import requests
from typing import List, Dict

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_data(self, endpoint: str) -> List[Dict]:
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []
