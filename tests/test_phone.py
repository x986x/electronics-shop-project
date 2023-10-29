import pytest

from src.phone import Phone


def test_phone():
    """Проверка вывода всех данных"""
    phone = Phone("test1", 40000, 10, 2)
    assert phone.name == "test1"
    assert phone.price == 40
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_number_of_sim_setter():
    """Проверка на изменение количества сим карт"""
    phone = Phone("test1", 4000, 10, 2)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2


def test_phone__error_number_of_sim():
    """Проверка на отрицательное и float количество сим карт"""
    with pytest.raises(ValueError):
        phone = Phone("test1", 500.75, 100,  2)
        phone1 = Phone("test2", 300.11, 100, 2.7)