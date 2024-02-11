import re
from typing import Callable

def generator_numbers(file_path: str):
    pattern = r'\b\d+\.\d+\b'  # Регулярний вираз для знаходження дійсних чисел
    with open(file_path, 'r') as file:
        text = file.read()  # Зчитуємо весь текст з файлу
        for match in re.finditer(pattern, text):
            yield float(match.group())  # Повертаємо дійсне число як float

def sum_profit(file_path: str, func: Callable):
    return sum(func(file_path))  # Сумуємо всі числа, що повертає генератор

file_path = "text.txt"  # Шлях до текстового файлу
total_income = sum_profit(file_path, generator_numbers)
print(f"Загальний дохід: {total_income}")
