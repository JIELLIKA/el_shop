from classes.item import Item


class MixingKey:

    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self) -> str:
        """Возвращаем текущую раскладку клавиатуры"""
        return self.__language

    def change_lang(self) -> None:
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class KeyBoard(Item, MixingKey):
    def __init__(self, name: str, price: int, quantity: int):
        """Инициализация экземпляров класса Клавиатура"""
        super().__init__(name, price, quantity)


kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb.item_name)
print(kb.language)
kb.change_lang()
print(kb.language)
kb.language = 'CH'
print(kb.language)