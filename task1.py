# объявляем константы, содержащие длительность секунд для минут, часов и дня
SEC_IN_MIN = 60
SEC_IN_HOUR = 3600
SEC_IN_DAY = 3600 * 24

# объявляем переменные содержащие наличие секунд, минут, часов и дней
sec = 0
min = 0
hour = 0
day = 0
time = []
duration = 0

# запуск цикла для множественного исполнения программы
while duration >= 0:
    print('Для выхода введите отрицательное число')
    duration = int(input('Введите длительность времени в секундах: ')) # запрашиваем у пользователя длительность
    # если длительность больше чем день
    if duration // SEC_IN_DAY > 0:
        day = duration // SEC_IN_DAY
        time.append(day)
        duration -= day * SEC_IN_DAY
        hour = duration // SEC_IN_HOUR
        time.append(hour)
        duration -= hour * SEC_IN_HOUR
        min = duration // SEC_IN_MIN
        time.append(min)
        sec = duration - min * SEC_IN_MIN
        time.append(sec)
        print(f'{day} дн {hour} час {min} мин {sec} сек')
    # если длительность меньше дня, но больше чем час
    elif duration // SEC_IN_HOUR > 0:
        hour = duration // SEC_IN_HOUR
        time.append(hour)
        duration -= hour * SEC_IN_HOUR
        min = duration // SEC_IN_MIN
        time.append(min)
        sec = duration - min * SEC_IN_MIN
        time.append(sec)
        print(f'{hour} час {min} мин {sec} сек')
    # если длительность меньше часа, но больше чем минута
    elif duration // SEC_IN_MIN > 0:
        min = duration // SEC_IN_MIN
        time.append(min)
        sec = duration - min * SEC_IN_MIN
        time.append(sec)
        print(f'{min} мин {sec} сек')
    # если длительность меньше минуты и больше 0
    elif not duration // SEC_IN_MIN > 0 and duration >= 0:
        sec = duration - min * SEC_IN_MIN
        time.append(sec)
        print(f'{sec} сек')
# если введено отрицательное число
else:
    print('Вы ввели неверное число в секундах!')

