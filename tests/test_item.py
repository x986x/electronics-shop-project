import pytest

import src.item
from src.item import Item, InstantiateCSVError

@pytest.fixture
def make_item():
    return Item("Компьютер", 5000, 3)

def test_calculate_total_price(make_item):
    item = make_item
    assert item.calculate_total_price() == 15_000
    assert item.calculate_total_price() == item.price * item.quantity


def test_apply_discount(make_item):
    item = make_item
    first_price = item.price
    item.apply_discount()
    assert item.price == first_price * Item.pay_rate
    assert item.price == 5000.0

    item.price = first_price
    item.pay_rate = 1.2
    item.apply_discount()
    assert item.price == first_price * item.pay_rate
    assert item.price == 6000.0

def test_set_name(make_item, capsys):
    item = make_item
    item.name = "Name"
    assert item.name == "Name"

    item.name = "NameNameNameNameName"
    output = capsys.readouterr()
    assert output.out == "Длина названия товара не" \
                         "должна превышать 10 символов\n"
    item.name = ""
    output = capsys.readouterr()
    assert output.out == "Длина названия должна иметь" \
                         "хотябы 1 символ\n"

def test_string_to_number():
    string = "343"
    assert Item.string_to_number(string) == 343

def test_repr():
    '''Проверка на ожидаемый результат по шаблону '''
    item = Item('test', 1000, 30)

    assert repr(item) == "Item('test', 1000, 30)"


def test_str():
    '''Проверка на ожидаемый результат по шаблону '''
    item = Item('test', 1000, 30)

    assert str(item) == 'test'


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл items.csv"):
        Item.instantiate_from_csv("items.csv")


def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError, match="Файл items.csv поврежден"):
        Item.instantiate_from_csv("../src/items.csv")