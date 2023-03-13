import pytest
from classes.phone import *

@pytest.fixture
def rnd_phone():
    return Phone("iPhone 14", 120_000, 10, 2)


def test_phone_num_sims(rnd_phone):
    """Тест на корректное определение количества сим-карт телефона"""
    assert rnd_phone.num_sims == 2

def test_phone_init(rnd_phone):
    """Тест на корректную инициализацию экземпляра класса Phone"""
    assert rnd_phone.quantity == 10