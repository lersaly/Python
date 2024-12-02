import collections
import string

def count_unique_words(text):
    """
    Подсчет количества уникальных слов в строке.
    
    :param text: Входная строка
    :return: Количество уникальных слов
    """
    # Удаляем знаки препинания
    # str.maketrans создает таблицу перевода, где каждый знак препинания заменяется на пробел
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    
    # Очищаем текст от препинаний, переводим в нижний регистр и разбиваем на слова
    cleaned_text = text.translate(translator).lower().split()
    
    # Используем Counter для подсчета уникальных слов
    word_counts = collections.Counter(cleaned_text)
    
    # Выводим количество уникальных слов
    print(f"Количество уникальных слов: {len(word_counts)}")
    
    return len(word_counts)

# Пример использования функции
def main():
    # Тестовые строки
    test_strings = [
        "Привет, мир! Привет, Python. Как дела?",
        "Раз два три четыре пять, шесть семь восемь.",
        "Повторяющиеся слова: слова слова повторяются.",
    ]
    
    # Тестирование функции
    for text in test_strings:
        print(f"\nИсходный текст: {text}")
        count_unique_words(text)

if __name__ == "__main__":
    main()