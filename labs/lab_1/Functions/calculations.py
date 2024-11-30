import math

def calculate(num1, num2, operator):
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
        else:
            raise ValueError("Невідомий оператор.")
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def special_operations(num1, operator):
    if operator == '√':
        return math.sqrt(num1)
    else:
        raise ValueError("Невідомий оператор.")
