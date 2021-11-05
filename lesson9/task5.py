class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):                                             # задали основной метод у родителя
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):                                             # переопределили методы у классов дочек
        print(f'Ручка {self.title} вышла на орбиту рисования')

class Pencil(Stationery):
    def draw(self):                                             # переопределили методы у классов дочек
        print(f'Карандаш {self.title} заточен и запущен в дело')

class Handle(Stationery):
    def draw(self):                                             # переопределили методы у классов дочек
        print(f'Маркер {self.title} замочен чернилами и приступил к мазюкам')

pencil = Pencil('TM')                                           # доказываем, что переопределение верно
pencil.draw()

pen = Pen('ErrickCrause')
pen.draw()

handle = Handle('Matic')
handle.draw()
