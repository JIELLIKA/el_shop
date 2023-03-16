import csv
import os
from classes.InstantiateCSVError import *


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
        """Возвращает информацию о наименовании, количестве и стоимости товара "для разработчика" """
        return f'Item("{self.__name}", "{self.price}", "{self.quantity}")'

    def __str__(self) -> str:
        """Возвращает информацию о наименовании, количестве и стоимости товара "для пользователя" """
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
        if not os.path.isfile('items.csv'):
            raise FileNotFoundError
        all_pos = []
        with open('items.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for pos in reader:
                for key, values in pos.items():
                    if key is None or values is None:
                        raise InstantiateCSVError
                all_pos.append((pos['name'] + " " + pos['price'] + " " + pos['quantity']))
            return all_pos


    @classmethod
    def new_init(cls, pos_list: str) -> "Item":
        name, price, quantity = pos_list.split(" ")
        return cls(name, price, quantity)

    @staticmethod
    def is_integer(num) -> bool:
        """Возвращает True, если число целое(5.0 - также целое число)"""
        new_type_num = str(num)
        new_num = new_type_num.split('.')
        if len(new_num) == 1:
            return True
        elif new_num[1] == '0':
            return True
        else:
            return False


if __name__ == "__main__":
    item = Item('Телевизор', 50000, 2)
    try:
        print(item.instantiate_from_csv())
    except FileNotFoundError as e:
        print(e)
    except InstantiateCSVError as e:
        print(e)
