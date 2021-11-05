class Road:

    def __init__(self, length, width):                                  # отпределяем класс и атрибуты
        self._length = length
        self._width = width
        print("Вы можете рассчитать массу полотна дороги используя метод weight.", '\n')

    def weight(self):
         thick = int(input('Введите толщину асфальта в см: '))          # вводим толщину асфальта
         weight_1cm = 25                                                # определяем внутренние переменные
         weight = self._length * self._width * weight_1cm * thick
         return print(f'Масса дороги: {self._length} м * {self._width} м * {weight_1cm} кг * {thick} см = {weight} т.')

Moscow_StPtrbg = Road(20, 5)
Moscow_StPtrbg.weight()