class Item:
    """Создаем класс для товара"""
    discount = 0.80

    def __init__(self, name, price, quantity):
        """Инициализация каждого экземпляра"""
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        """Возвращает полную стоимость товара"""
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self):
        """Применение скидки к товару"""
        self.price = self.price * self.discount

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

item1.apply_discount()
print(item1.price)
print(item2.price)