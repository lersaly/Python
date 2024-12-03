from datetime import datetime, timedelta

def datetime_tasks():
#Отображение текущей даты и времени
    current_datetime = datetime.now()
    print(f"Текущая дата и время: {current_datetime}")
    print(f"Форматированный вывод: {current_datetime.strftime('%d.%m.%Y %H:%M:%S')}")

#Вычисление разницы между двумя датами
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2024, 2, 2)
    date_difference = date2 - date1
    print(f"Разница между датами: {date_difference.days} дней")

#Преобразование строки в объект даты и времени
    date_string = "15.06.2023 14:30:00"
    parsed_date = datetime.strptime(date_string, "%d.%m.%Y %H:%M:%S")
    print(f"Parsed date: {parsed_date}")
    print(f"День недели: {parsed_date.strftime('%A')}")

if __name__ == "__main__":
    datetime_tasks()