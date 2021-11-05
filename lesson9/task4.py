class Car:
    def __init__(self, speed, color, name, is_police):  # задаем атрибуты родительского класса
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):                                       # определяем методы родительского класса
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')

class TownCar(Car):                                     # переопределяем метод в этом классе
    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'{self.name} вы превысили разрешенную скорость. Ваша скорость: {self.speed}')
        else:
            print(f'Машина {self.name} едет со скоростью {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):                                     # переопределяем метод в этом классе
    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'{self.name} вы превысили разрешенную скорость. Ваша скорость: {self.speed}')
        else:
            print(f'Машина {self.name} едет со скоростью {self.speed}')

class PoliceCar(Car):
    pass

tracktor = WorkCar(20, 'green', 'Taylor', False)                # проверяем работу скрипта
print(tracktor.name, tracktor.color, tracktor.speed)
tracktor.go()
tracktor.turn('направо')
tracktor.stop()
tracktor.show_speed()                                           # скорость до превышения
tracktor.speed = 70
tracktor.show_speed()                                           # вывод после превышения
print("-----------------")
police = PoliceCar(90, 'white-blue', 'Rembo', True)
print(police.name, police.color, police.speed)
police.go()
police.turn('налево')
police.show_speed()                                             # для этого объекта не работает переопределнный метод
police.speed = 110
police.show_speed()
