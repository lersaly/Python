import requests
from bs4 import BeautifulSoup

# URL для получения данных
url = "https://github.com/lersaly/system_design"  # Замените на нужный URL

# Добавим заголовки, чтобы запрос выглядел как от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Получение данных с веб-сайта
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверка на ошибки

    # Выводим HTML-код страницы для диагностики
    print(response.text)  # Это покажет весь HTML-код страницы

    # Парсинг HTML-кода
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример извлечения данных: получение заголовков <h1>
    headers = soup.find_all('h1')
    if headers:
        print("Заголовки на странице:")
        for header in headers:
            print(header.text)
    else:
        print("Заголовков <h1> не найдено")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе данных: {e}")

except Exception as e:
    print(f"Общая ошибка: {e}")


