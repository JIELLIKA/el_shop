import pytest
from classes.item import Item
@pytest.fixture
def rnd_item():
    return Item('Телевизор', 50000, 2)


def test_item_init(rnd_item):
    """Тестирование на корректную инициализацию экземпляра класса Item"""
    assert rnd_item.price == 50000
    assert rnd_item.quantity == 2


def test_item_calculate_total_price(rnd_item):
    """Тестирование на корректный расчет итоговой стоимости"""
    check_total_price = rnd_item.price * rnd_item.quantity
    assert check_total_price == 100000


def test_item_apply_discount(rnd_item):
    """Тестирование на корректную цену товара с учетом скидки"""
    check_price = rnd_item.price * rnd_item.discount
    assert check_price == 40000


def test__repr(rnd_item):
    """Тестирование на корректную инициализацию экземпляра класса Item с помощью магического метода __repr__"""
    assert rnd_item.__repr__() == 'Item("Телевизор", "50000", "2")'


def test_item_name(rnd_item):
    """Тестирование на корректную инициализацию экземпляра класса Item с учетом декоратора property"""
    assert rnd_item.item_name == 'Телевизор'

def test_item_is_integer():
    """Тестирование на корректное отображение чисел. Все числа представлены в формате целых чисел"""
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.5) == False
    assert Item.is_integer(5.0) == True