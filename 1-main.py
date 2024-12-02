# main.py
from my_math_package import NumberCalculator

def main():
    # Пример использования класса NumberCalculator
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [10.5, 20.3, 30.2]
    
    try:
        # Вычисление суммы для первого списка
        result1 = NumberCalculator.sum_numbers(numbers1)
        print(f"Сумма чисел в списке {numbers1}: {result1}")
        
        # Вычисление суммы для второго списка
        result2 = NumberCalculator.sum_numbers(numbers2)
        print(f"Сумма чисел в списке {numbers2}: {result2}")
        
        # Попытка вызвать с некорректным аргументом
        # NumberCalculator.sum_numbers("not a list")  # Раскомментируйте для проверки обработки ошибок
        # NumberCalculator.sum_numbers([1, 2, "3"])  # Раскомментируйте для проверки обработки ошибок
    
    except TypeError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()