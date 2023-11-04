import pytest
from src.keyboard import Keyboard


def test_name():
    """Проверка вывода наименования"""
    kb = Keyboard('test1', 9600, 5)
    assert str(kb) == "test1"


def test_language_EN():
    kb = Keyboard('test1', 9600, 5)
    assert str(kb.language) == "EN"


def test_language_RU():
    kb = Keyboard('test1', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_change_language():
    try:
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        kb.language = 'CH'
    except AttributeError as i:
        assert str(i) == "property 'language' of 'Keyboard' object has no setter"