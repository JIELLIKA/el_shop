import pytest
from main import Item

@pytest.fixture
def rnd_item():
    return Item('Телевизор', 50000, 2)

def test_item_init(rnd_item):
    assert rnd_item.name == 'Телевизор'
    assert rnd_item.price == 50000
    assert rnd_item.quantity == 2

def test_item_calculate_total_price(rnd_item):
    check_total_price = rnd_item.price * rnd_item.quantity
    assert check_total_price == 100000

def test_item_apply_discount(rnd_item):
    check_price = rnd_item.price * rnd_item.discount
    assert check_price == 40000