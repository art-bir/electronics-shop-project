"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


# @pytest.mark.skip(reason="no way of currently testing this")
# @pytest.mark.parametrize("name, price, quantity, expected",
#                          [("Кабель", 10, 5, []),
#                           ("Мышка", 50, 5, [])])
# def test_item_(name, price, quantity, expected):
#     assert Item(name, price, quantity).all == []


@pytest.mark.parametrize("name, price, quantity",
                         [("Мышка", 50, 5)])
def test_item(name, price, quantity):
    item = Item(name, price, quantity)
    assert isinstance(item, Item)
    assert isinstance(item.all, list)
    assert item.name == name and item.price == price and item.quantity \
           == quantity

