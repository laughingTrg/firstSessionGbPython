

def val_checker(func_lambda):                   # создали декоратор с функцией лямбда

    def _val_checker(func1):                    # создает декоратор с декорируемой функцией
        def wrapper(*args):                     # передаем в обертку аргументы
            arg = (str(*args))                  # присваиваем текущий аргумент переменной
            if func_lambda(*args):              # если лямбда функция с аргументом - истина
                result = func1(*args)           # присваиваем результат
                return print(result)            # выводим результат
            else:                               # иначе
                msg = f'wrong val {arg}'        # создаем ошибочное сообщение
                raise ValueError(msg)           # вызываем метод ValueError с сохраненным сообщением
        return wrapper                          # возвращаем обертку
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

calc_cube(5)
calc_cube(-5)