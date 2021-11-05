class TrafficLight:                                             # родительский класс создаем
    def __init__(self):
        self.__color = ''                                       # создаем приватную переменную с цветом
        print('Объект светофора идентифицирован. Светофор ожидает запуска.', '\n')

    def __light_count(self, time_light):                        # объявляем приватную функцию
        import time                                             # только для внутреннего пользования
        for i in range(time_light):                             # показывает отсчет текущего цвета
            print(time_light - i)
            time.sleep(1)
        print()

    def running(self):                                          # метод запуска светофора
        light_color = ['Красный:', 'Желтый:', 'Зеленый:']       # задаем параметры спискам с цветом
        light_time = [7, 2, 5]                                  # и длительностью
        for color, time in zip(light_color, light_time):        # проходим по списками
            self.__color = color                                # присваиваем атрибуту цвет и запускаем
            print(self.__color)                                 # приватную функцию
            self.__light_count(time)


traffic_light = TrafficLight()                                  # проверка работы скрипта
traffic_light.running()