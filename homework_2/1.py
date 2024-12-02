def read_numeric_lines(filename):
    """
    Читает файл и обрабатывает строки с числовыми и нечисловыми значениями.
    
    :param filename: Путь к файлу
    :raises FileNotFoundError: Если файл не найден
    """
    try:
        # Открываем файл с указанием кодировки
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем все строки
            data = file.readlines()
            
            # Список для хранения числовых строк
            numeric_lines = []
            
            # Обработка каждой строки
            for line in data:
                # Удаляем символы перевода строки и пробелы
                line = line.strip()
                
                # Проверяем, является ли строка полностью числом
                if line.replace('.', '', 1).isdigit():
                    # Если строка полностью состоит из цифр или числа с точкой
                    print(line)
                    numeric_lines.append(line)
                else:
                    # Выводим сообщение об ошибке для каждой нечисловой строки
                    print("Строка содержит не только числа")
            
            return numeric_lines
    
    except FileNotFoundError:
        # Обработка ситуации, когда файл не найден
        raise FileNotFoundError(f"Файл {filename} не найден")

# Пример использования функции
def main():
    try:
        # Пример файла data.txt
        # Возможное содержимое файла:
        # 10
        # hello world
        # test123
        # 20
        
        result = read_numeric_lines('homework_2/data.txt')
        print("Числовые строки:", result)
    
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

# homework_2/data.txt