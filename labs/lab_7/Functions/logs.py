import logging
from colorama import Fore

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Logging:
    @staticmethod
    def log_request(request_type: str, endpoint: str, status: str):
        logging.info(f"{request_type} request to {endpoint} - Status: {status}")

class ErrorHandler:
    @staticmethod
    def handle_error(error_message: str):
        print(f"{Fore.RED}Error: {error_message}")
