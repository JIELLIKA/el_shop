import csv


class Item:
    """Создаем класс для товара"""
    discount = 0.80

    def __init__(self, name: str, price: int, quantity: int):
        """Инициализация каждого экземпляра"""
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self) -> str:
        return f'Item("{self.__name}", "{self.price}", "{self.quantity}")'

    def __str__(self) -> str:
        return f'{self.__name}, {self.price}, {self.quantity}'

    @property
    def item_name(self) -> str:
        """Возвращаем текущее название позиции"""
        return self.__name

    @item_name.setter
    def item_name(self, value: str) -> None:
        """Проверяем, чтобы длина наименования товара не превышала 10 символов"""
        if len(value) > 10:
            raise Exception("Длина наименования товара превышает 10 символов")
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



