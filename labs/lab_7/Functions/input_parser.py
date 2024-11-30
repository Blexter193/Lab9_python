import re
from typing import List

class InputParser:
    @staticmethod
    def parse_phone_numbers(text: str) -> List[str]:
        return re.findall(r'\+?\d{10,15}', text)

    @staticmethod
    def parse_dates(text: str) -> List[str]:
        return re.findall(r'\d{4}-\d{2}-\d{2}', text)
