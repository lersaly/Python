from itertools import count, starmap, chain

def safe_next(iterator, default=None):
    """Безопасное получение следующего элемента из итератора"""
    try:
        return next(iterator)
    except StopIteration:
        return default

def itertools_tasks():
    try:
    #Бесконечный генератор с обработкой исключений
        numbers_generator = count(start=1, step=2)
        print("Первые 5 нечетных чисел:")
        safe_numbers = [safe_next(numbers_generator) for _ in range(5)]
        print(safe_numbers)

    #Применение функций к итератору с защитой
        empty_iterator = iter([])
        try:
            result = list(map(lambda x: x**2, empty_iterator))
        except StopIteration:
            print("Пустой итератор обработан корректно")

    #Объединение итераторов с проверкой
        iterator1 = [1, 3]
        iterator2 = []
        combined_iterator = chain(iterator1, iterator2)
        
        try:
            combined_list = list(combined_iterator)
            print("Объединенный итератор:", combined_list)
        except Exception as e:
            print(f"Ошибка объединения итераторов: {e}")

    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    itertools_tasks()