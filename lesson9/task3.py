class Worker:                                                   # задаем родительский класс и переменные
    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):                                         # дочерний класс
    def get_full_name(self):                                    # внутренние методы
        print(self.surename, self.name)

    def get_total_income(self):
        print('Доход с учетом премии:', sum(self._income.values()))

first = Position('Max', 'Smith', 'engeneer', 1000, 500)         # объявляем объект дочернего класса
first.get_full_name()                                           # прорверяем работу скрипта
first.get_total_income()
second = Position('Lisa', 'May', 'HR', 2000, 300)
second.get_full_name()
second.get_total_income()
