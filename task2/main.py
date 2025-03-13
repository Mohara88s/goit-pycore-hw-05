from typing import Callable
import re

def generator_numbers(text: str)-> float:
    pattern = r"\b\d+\.\d+\b"
    for income in re.findall(pattern, text):
        yield float(income)

def sum_profit(text: str, func: Callable[[str],float])-> float:
    total_profit = sum(func(text))
    return total_profit
    

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# Загальний дохід: 1351.46
