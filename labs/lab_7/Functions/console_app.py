import json
import csv
from tabulate import tabulate
from colorama import Fore, Style, init
from typing import List, Dict
from labs.lab_7.Functions.repository import Repository

class ConsoleApp:
    def __init__(self, repository: Repository):
        self.repository = repository
        init(autoreset=True)

    def display_data(self, data: List[Dict], title: str):
        if data:
            print(f"{Fore.GREEN}{Style.BRIGHT}{title}")
            headers = data[0].keys()
            rows = [d.values() for d in data]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print(f"{Fore.RED}No data available.")

    def get_user_choice(self):
        print("1. Show Posts\n2. Show Users\n3. Save Data\n4. Exit")
        return input("Enter your choice: ")

    def run(self):
        while True:
            choice = self.get_user_choice()
            if choice == '1':
                self.display_data(self.repository.get_posts(), "Posts")
            elif choice == '2':
                self.display_data(self.repository.get_users(), "Users")
            elif choice == '3':
                self.save_data_option()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def save_data_option(self):
        data = self.repository.get_posts()
        file_format = input("Choose format to save (json/csv/txt): ").strip().lower()
        filename = f"data.{file_format}"
        if file_format == "json":
            self.save_json(data, filename)
        elif file_format == "csv":
            self.save_csv(data, filename)
        elif file_format == "txt":
            self.save_txt(data, filename)
        else:
            print("Invalid format. Please choose json, csv, or txt.")

    @staticmethod
    def save_json(data: List[Dict], filename: str):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")

    @staticmethod
    def save_csv(data: List[Dict], filename: str):
        with open(filename, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}")

    @staticmethod
    def save_txt(data: List[Dict], filename: str):
        with open(filename, "w") as file:
            for entry in data:
                file.write(str(entry) + "\n")
        print(f"Data saved to {filename}")
