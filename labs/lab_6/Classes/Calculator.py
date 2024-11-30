import math

class BaseCalculator:
    def __init__(self):
        self.memory = None
        self.history = []

    def get_user_input(self):
        raise NotImplementedError()

    def validate_operator(self, operator):
        raise NotImplementedError()

    def perform_calculation(self, num1, num2, operator):
        raise NotImplementedError()

    def ask_repeat(self):
        raise NotImplementedError()

    def run(self):

        raise NotImplementedError()


class Calculator(BaseCalculator):
    def __init__(self):
        super().__init__()

    def get_user_input(self):
        num1 = input("Введіть перше число (або 'm' для використання пам'яті): ")
        if num1.lower() == 'm' and self.memory is not None:
            num1 = self.memory
            print(f"Використано з пам'яті: {num1}")
        else:
            num1 = float(num1)

        operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")

        if operator != '√':
            num2 = input("Введіть друге число (або 'm' для використання пам'яті): ")
            if num2.lower() == 'm' and self.memory is not None:
                num2 = self.memory
                print(f"Використано з пам'яті: {num2}")
            else:
                num2 = float(num2)
        else:
            num2 = None

        return num1, num2, operator

    def validate_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '^', '%', '√']
        if operator not in valid_operators:
            print("Невірний оператор. Спробуйте ще раз.")
            return False
        return True

    def perform_calculation(self, num1, num2, operator):
        try:
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                return num1 / num2
            elif operator == '^':
                return num1 ** num2
            elif operator == '%':
                return num1 % num2
            elif operator == '√':
                return math.sqrt(num1)
        except Exception as e:
            print(f"Помилка: {e}")
            return None

    def ask_repeat(self):
        repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower()
        return repeat == 'так'

    def run(self):
        print("Ласкаво просимо до калькулятора!")
        while True:
            num1, num2, operator = self.get_user_input()

            if not self.validate_operator(operator):
                continue

            result = self.perform_calculation(num1, num2, operator)

            if result is not None:
                print(f"Результат: {result}")
                self.memory = result  # Зберігаємо результат у пам'ять
                self.history.append(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")

            if not self.ask_repeat():
                break

        if self.history:
            print("\nІсторія обчислень:")
            for record in self.history:
                print(record)