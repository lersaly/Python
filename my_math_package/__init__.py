# my_math_package/__init__.py
# Импортируем класс из модуля calculator
from .calculator import NumberCalculator

# Можно явно указать, что именно экспортируется
__all__ = ['NumberCalculator']