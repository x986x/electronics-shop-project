from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.
        :param name: Название смартфона.
        :param price: Цена за единицу смартфона.
        :param quantity: Количество смартфонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Магический метод __repr__
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        Магический метод __str__
        """
        return self.name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        '''
        Устснавливает значение поддерживаемых
        сим-карт, проверяя является ли значение
        положительным. В конечном итоге возвращает
        целое от числа или ошибку, если значение окажется
        отрицательным
        '''
        if isinstance(value, int) and value > 0:
            self.__number_of_sim = int(value)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')