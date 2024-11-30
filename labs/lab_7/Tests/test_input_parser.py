import unittest
from labs.lab_7.Functions.input_parser import InputParser

class TestInputParser(unittest.TestCase):
    def test_parse_phone_numbers(self):
        text = "Contact +1234567890 and +0987654321."
        self.assertEqual(InputParser.parse_phone_numbers(text), ["+1234567890", "+0987654321"])

    def test_parse_dates(self):
        text = "The event is on 2023-12-31."
        self.assertEqual(InputParser.parse_dates(text), ["2023-12-31"])

if __name__ == '__main__':
    unittest.main()