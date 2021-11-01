from functools import wraps

def type_logger(func):
    log_list = []                                                               # создаем список для хранения аргументов

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal log_list                                                       # подключаем список
        name_kwarg = str(*kwargs.values())                                      # сохраняем аргументы в переменные
        name_arg = str(*args)
        result = func(*args, **kwargs)                                          # получаем результат оборачиваемой функции
        print(f'Тип значения функции {func.__name__}: {type(result)}')          # выводим имя оборачиваемой функции и тип результата
        if kwargs: log_list.append(f'{name_kwarg}: {type(*kwargs.values())}')   # если именуемые переменные добавляем в список
        else: log_list.append(f'{name_arg}: {type(*args)}')                     # иначе добавляем неименуемые переменные
        print(func.__name__ + '(', end='')                                      # выводим результат в требуемом формате
        print(*log_list, end='', sep=', ')
        print(')')
        return result
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(x=5)                                                              # пробуем на примерах
b = calc_cube(6)
c = calc_cube(7)