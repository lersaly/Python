import logging
from datetime import datetime

logging.basicConfig(
    filename='warehouse.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def increase_quantity(self, amount):
        self.quantity += amount
        logging.info(f"Увеличено количество товара '{self.name}' на {amount}")
    
    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            logging.info(f"Уменьшено количество товара '{self.name}' на {amount}")
            return True
        return False
    
    def calculate_cost(self, amount):
        return amount * self.price

class Warehouse:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                existing_product.increase_quantity(product.quantity)
                return
        self.products.append(product)
        logging.info(f"Добавлен новый товар '{product.name}' в количестве {product.quantity}")
    
    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]
        logging.info(f"Товар '{product_name}' удален со склада")
    
    def calculate_total_cost(self):
        return sum(product.price * product.quantity for product in self.products)

class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_history = []
    
    def sell_product(self, warehouse, product_name, quantity):
        for product in warehouse.products:
            if product.name == product_name:
                if product.decrease_quantity(quantity):
                    sale_revenue = product.calculate_cost(quantity)
                    sale_record = {
                        'date': datetime.now(),
                        'product': product_name,
                        'quantity': quantity,
                        'revenue': sale_revenue
                    }
                    self.sales_history.append(sale_record)
                    logging.info(f"Продан товар '{product_name}' в количестве {quantity}")
                    return sale_revenue
                else:
                    print(f"Недостаточно товара '{product_name}' на складе")
                    return 0
        print(f"Товар '{product_name}' не найден на складе")
        return 0
    
    def sales_report(self):
        print("Отчет о продажах:")
        for sale in self.sales_history:
            print(f"Дата: {sale['date']}, "
                  f"Товар: {sale['product']}, "
                  f"Количество: {sale['quantity']}, "
                  f"Выручка: {sale['revenue']} руб.")

# Пример использования
def main():
    warehouse = Warehouse()

    warehouse.add_product(Product("Яблоки", 100, 50))
    warehouse.add_product(Product("Бананы", 80, 70))
    warehouse.add_product(Product("Апельсины", 50, 60))

    seller = Seller("Иван")

    seller.sell_product(warehouse, "Яблоки", 20)
    seller.sell_product(warehouse, "Бананы", 15)

    seller.sales_report()

    print(f"Общая стоимость товаров на складе: {warehouse.calculate_total_cost()} руб.")

if __name__ == "__main__":
    main()