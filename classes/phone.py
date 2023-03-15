from classes.item import Item
class Phone(Item):
    def __init__(self, name: str, price: int, quantity: int, num_sim_card: int):
        """Инициализация экземпляров класса Телефон"""
        super().__init__(name, price, quantity)
        self.__num_sim_card = num_sim_card

    @property
    def num_sims(self) -> int:
        """Возвращаем текущее количество сим-карт"""
        return self.__num_sim_card

    @num_sims.setter
    def num_sims(self, value: int) -> None:
        """Реализуем проверку, что количество сим-карт не может быть меньше или равно 0"""
        if value <= 0 or type(value) != int:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__num_sim_card = value

    def __add__(self, other) -> int:
        """Складываем экземпляры классов по количеству товара"""
        if isinstance(self, Phone) and isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Возможно только сложение экземпляров класса Item или Phone")


# if __name__ == "__main__":
#     item = Item("iPhone 14", 120_000, 5)
#     phone = Phone("iPhone 14", 120_000, 10, 2)
#     print(phone.num_sims)
#     print(repr(phone))
#     phone.num_sims = 3
#     print(phone.num_sims)
#     print(phone + item)