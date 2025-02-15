import os
import subprocess
from labs.lab_1 import runner as run_lab1
from labs.lab_2 import runner as run_lab2
from labs.lab_3 import runner as run_lab3
from labs.lab_4 import runner as run_lab4
from labs.lab_5 import runner as run_lab5
from labs.lab_6 import runner as run_lab6
from labs.lab_7 import runner as run_lab7

class LabRunner:
    def __init__(self):
        self.labs = {
            1: run_lab1,
            2: run_lab2,
            3: run_lab3,
            4: run_lab4,
            5: run_lab5,
            6: run_lab6,
            7: run_lab7
        }

    def run_lab(self, lab_number):
        try:
            if lab_number in self.labs:
                print(f"Запускаємо лабораторну роботу №{lab_number}...")
                self.labs[lab_number]()
            else:
                print("Некоректний номер лабораторної роботи.")
        except AttributeError:
            print(f"Помилка: лабораторна робота №{lab_number} не має коректної функції main.")

    def run_tests(self, lab_number):
        """
        Запуск юніт-тестів для вказаної лабораторної роботи.
        """
        test_files = {
            6: "labs/lab_6/Tests",
        }
        test_file = test_files.get(lab_number)
        if not test_file:
            print(f"Для лабораторної роботи №{lab_number} тести не знайдено.")
            return

        if os.path.exists(test_file):
            print(f"Запускаємо тести для лабораторної роботи №{lab_number}...")
            subprocess.run(["python", "-m", "unittest", test_file])
        else:
            print(f"Файл з тестами не знайдено: {test_file}.")

if __name__ == "__main__":
    runner = LabRunner()
    while True:
        try:
            print("\nМеню:")
            print("1-7: Запуск лабораторної роботи")
            print("8: Запуск тестів для 6-ї лабораторної")
            print("9: Вихід")
            choice = int(input("Введіть номер дії: "))

            if choice == 0:
                break
            elif choice == 9:
                runner.run_tests(6)
            elif choice == 10:
                runner.run_tests(7)
            elif 1 <= choice <= 8:
                runner.run_lab(choice)
            else:
                print("Некоректний вибір.")
        except ValueError:
            print("Помилка: введіть коректне число.")
