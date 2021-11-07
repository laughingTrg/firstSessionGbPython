class Cell:                                                         # создаем базовый класс Клетка
    def __init__(self, cell_count):                                 # определяем аттрибут - количество клеток
        self._cell_count = int(cell_count)

    def __call__(self, *args, **kwargs):                            # перегружаем вызов объекта для получения значения клеток
        return self._cell_count

    def __str__(self):                                              # перегружаем метод строки для вывода количвества клеток
        return str(self._cell_count)

    def __add__(self, other):                                       # перегружаем метод сложения для сложения объектов и получения результата
        return Cell(self._cell_count + other())

    def __sub__(self, other):                                       # метод вычитания получаем новую клетку с оставшимся количеством клеток
        if self._cell_count - other() < 0:
            raise ValueError('Исходная клетка меньше вычитаемой')
        return Cell(self._cell_count - other())

    def __mul__(self, other):                                       # метод умножения получаем клетку с умноженным колеством
        return Cell(self._cell_count * other())

    def __floordiv__(self, other):                                  # метод деления получаем целое число после деления и клетку
        return Cell(int(self._cell_count % other()))

    def __truediv__(self, other):
        return Cell(int(self._cell_count / other()))

    def make_order(self, cell_in_row):                              # метод вывода результата
        for _ in range(int(self._cell_count / cell_in_row)):
                print('*' * cell_in_row)
        print('*' * (self._cell_count % cell_in_row))

cell_1 = Cell(2)                                                    # создаем 2 объекта класса
cell_2 = Cell(3)
cell_add = cell_1 + cell_2                                          # получаем сложение
print('Клетка в результате сложения клеток', cell_add)

cell_sub = cell_add - cell_1                                        # вычитание
print('Клетка в результате вычитаяни клеток', cell_sub)

cell_mul = cell_1 * cell_add                                        # умножение
print('Клетка в результате умножения клеток', cell_mul)

cell_div = cell_mul / cell_2                                        # деление
print('Клетка в результате деления клеток', cell_div)

cell_mul.make_order(4)                                              # вывод количества клеток