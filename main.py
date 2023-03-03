import csv


class Item:
    """Создаем класс для товара"""
    discount = 0.80

    def __init__(self, name: str, price: int, quantity: int):
        """Инициализация каждого экземпляра"""
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def item_name(self) -> str:
        """Возвращаем текущее название позиции"""
        return self.__name

    @item_name.setter
    def len_name(self, value: str) -> None:
        if len(value) > 10:
            print("Exception: Длина наименования товара превышает 10 символов")
        else:
            self.__name = value

    def calculate_total_price(self):
        """Возвращает полную стоимость товара"""
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self):
        """Применение скидки к товару"""
        self.price = self.price * self.discount

    @classmethod
    def instantiate_from_csv(cls):
        """Получаем список товара из файла. Преобразуем в формат для последующей инициализации"""
        all_pos = []
        with open('items.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for pos in reader:
                all_pos.append((pos['name'] + " " + pos['price'] + " " + pos['quantity']))
            # print(all_pos)
        return all_pos

    @classmethod
    def new_init(cls, pos_list: str) -> "Item":
        name, price, quantity = pos_list.split(" ")
        return cls(name, price, quantity)

    @staticmethod
    def is_integer(num) -> bool:
        new_type_num = str(num)
        new_num = new_type_num.split('.')
        if len(new_num) == 1:
            return True
        elif new_num[1] == '0':
            return True
        else:
            return False


item1 = Item('Телефон', 10000, 5)
item1.len_name = 'Смартфон'
print(item1.len_name)
item1.len_name = 'Телефон'
print(item1.len_name)

list_of_items = Item.instantiate_from_csv()
item1 = Item.new_init(list_of_items[2])
print(item1.len_name)

print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))