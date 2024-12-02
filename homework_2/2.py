class DataBuffer:
    """
    Класс для управления буфером данных с ограничением на количество элементов(5).
    """
    def __init__(self, max_size=5):
        self.buffer = []
        self.max_size = max_size
    
    def add_data(self, data):
        """
        Добавление данных в буфер.
        
        :param data: Данные для добавления
        """
        if len(self.buffer) >= self.max_size:
            print("Буфер переполнен. Очистка...")
            self.buffer.clear()
        
        self.buffer.append(data)
        print(f"Добавлено значение: {data}")
        print(f"Текущее состояние буфера: {self.buffer}")
    
    def get_data(self):
        """
        Получение данных из буфера.
        
        :return: Список данных в буфере
        """
        if not self.buffer:
            print("Буфер пуст. Нет данных для извлечения.")
            return None
        
        return self.buffer.copy()

# Пример использования класса DataBuffer
def main():
    # Создаем буфер с максимальным размером 5
    buffer = DataBuffer()
    
    # Демонстрация работы методов
    buffer.add_data(10)
    buffer.add_data("hello")
    buffer.add_data(15.5)
    buffer.add_data([1, 2, 3])
    buffer.add_data({"key": "value"})
    
    # Попытка добавить шестой элемент (вызовет очистку буфера)
    buffer.add_data(20)
    
    # Получение данных из буфера
    data = buffer.get_data()
    print("Данные в буфере:", data)
    
    # Создаем новый пустой буфер
    empty_buffer = DataBuffer()
    
    # Попытка получить данные из пустого буфера
    empty_buffer.get_data()

if __name__ == "__main__":
    main()