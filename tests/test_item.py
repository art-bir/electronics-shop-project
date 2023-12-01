"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


@pytest.mark.parametrize("name, price, quantity",
                         [("Мышка", 50, 5)])
def test_item(name, price, quantity):
    item = Item(name, price, quantity)
    assert isinstance(item, Item)
    assert isinstance(item.all, list)
    assert item.name == name and item.price == price and item.quantity \
           == quantity


@pytest.mark.parametrize("name, price, quantity",
                         [("Мышка", 50, 5)])
def test_calculate_total_price(name, price, quantity):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == price * quantity


@pytest.mark.parametrize("name, price, quantity",
                         [("Мышка", 50, 5)])
def test_apply_discount(name, price, quantity):
    item = Item(name, price, quantity)
    item.apply_discount()
    assert item.price == price * Item.pay_rate


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    assert item.name == 'СуперСмарт'
    assert len(item.name) <= 10


def test_instantiate_from_csv():
    Item.instantiate_from_csv('tests/test.csv')
    assert len(Item.all) == 5

@pytest.mark.parametrize("value, expected", [('5', 5), ('5.0', 5), ('5.5', 5)])
def test_string_to_number(value, expected):
    assert Item.string_to_number(value) == expected
