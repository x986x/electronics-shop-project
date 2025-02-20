import csv
import codecs


class InstantiateCSVError(Exception):
    pass

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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __add__(self, other):
        '''
        Складывает два обьекты, относящиеся к
        классу Item или его подклассам
        '''
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """ Сложение количества товаров из классов Item и Phone"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Складывать можно только объекты классов с родительским классом Item")

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
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Возвращает имя товара
        :return: имя товара
        """
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Устанавливает имя товара, проверяя,
        что имя более 1 символа и не привышает 10
        символов
        """
        if len(value) > 10:
            print("Длина названия товара не"
                  "должна превышать 10 символов")
        elif len(value) == 0:
            print("Длина названия должна иметь"
                  "хотябы 1 символ")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        '''инициализируем экземпляры класса Item данными из файла src/items.csv'''
        cls.all.clear()  # очистка списка перед загрузкой данных из файла csv
        try:
            with codecs.open(filename, 'r', encoding='windows-1251', errors='replace') as f:
                reader = csv.DictReader(f)
                items = []
                for row in reader:
                    #if 'name' not in row or 'price' not in row or 'quantity' not in row:
                    if row['name'] == '' or row['price'] == '' or row['quantity'] == '':
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    else:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        item = cls(name, price, quantity)
                        items.append(item)

                cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")


    @staticmethod
    def string_to_number(str_number: str) -> int:
        number = str_number.split('.')
        return int(number[0])