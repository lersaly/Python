# my_math_package/calculator.py
class NumberCalculator:
    """
    Класс для выполнения математических операций со списками чисел.
    """
    @staticmethod
    def sum_numbers(numbers):
        """
        Вычисляет сумму всех чисел в передаваемом списке.
        
        :param numbers: Список чисел
        :return: Сумма всех чисел в списке
        """
        if not isinstance(numbers, list):
            raise TypeError("Аргумент должен быть списком")
        
        try:
            return sum(numbers)
        except TypeError:
            raise TypeError("Список должен содержать только числа")