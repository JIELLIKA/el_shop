import pytest
from classes.keyboard import *

@pytest.fixture()
def rnd_keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)

def test_keyboard_init(rnd_keyboard):
    """Тестирование на корректную инициализацию экземпляра класса KeyBoard"""
    assert rnd_keyboard.quantity == 5
    assert rnd_keyboard.language == 'EN'

def test_keyboard_change_lang(rnd_keyboard):
    """Тестирование на корректную смену раскладки клавиатуры"""
    rnd_keyboard.change_lang()
    assert rnd_keyboard.language == 'RU'