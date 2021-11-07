class Clothes:                                                          # базовый класс одежда с названием
    def __init__(self, name):
        self.name = name

    @property                                                           # задаем обязательное условие переопределения метода для дочек
    def consumption_cloth(self):
        pass

class Suit(Clothes):                                                    # дочерний класс
    def __init__(self, name, size):                                     # описываем класс инит для костюма
        super().__init__()
        self._size = size                                               # задаем аттрибут - размер

    def consumption_cloth(self):                                        # определяем метод расчета затрат н ткань
        from decimal import Decimal
        return Decimal(self._size/6.5 + 0.5).quantize(Decimal('1.00'))  # возвращаем количество ткани по формуле приводим к 2 знакам после запятой

class Coat(Clothes):                                                    # дочка
    def __init__(self, name, height):                                   # описываем класс инит для пальто
        super().__init__()
        self._height = height

    def consumption_cloth(self):                                        # переопределяем метод расчета затрат на ткань для пальто
        from decimal import Decimal
        return Decimal(self._height * 2 + 0.3).quantize(Decimal('1.00'))# возвращаем полученное значение по формуле

suit = Suit('Gucci', 1000)                                              # создаем экземпляр класса костюм
print(suit.consumption_cloth())                                         # выводим количество потраченного материала
coat = Coat('Marco Massini', 175)                                       # создаем экземпляр класса пальто
print(coat.consumption_cloth())                                         # выводим количество потраченного материала