import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            value = value[:10]
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, csvfile: str) -> None:
        """
        Создание экземпляра класса item из файла.

        :param csvfile: Путь к файлу с данными по товарам.
        """
        cls.all = []
        with open(csvfile, mode='r', encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразование строки в число.

        :param value: Преобразованная строка.
        :return: Преобразованное число.
        """
        return int(float(value))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
