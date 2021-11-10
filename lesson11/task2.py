class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        print('Программа деления двух чисел. Для выхода введите букву')
        divisible = int(input('Введите делимое число: '))
        divider = int(input('Введите число делитель: '))
        if divider == 0:
            raise DivZero('Вы пытаетесь разделить на 0. На 0 делить нельзя! Попробуйте еще раз.\n')
        result = divisible / divider
    except DivZero as err:
        print(err)
    except ValueError:
        print('Вы вышли из программы! Удачного дня!')
        break
    else:
        print("Результат деления:", result, '\n')