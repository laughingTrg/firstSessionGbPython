def odd_nums(max_num):                                                  # создаем функцию вывода нечетных чисел от 1 до n
    for num in range(1, max_num + 1, 2):                                # делаем генератор через цикл for и yield
        yield print(num)
odd_to_15 = odd_nums(15)                                                # присваиваем переменной значения функции (генератор)

while True:                                                             # проверяем работу генератора до ошибки StopIteration
    next(odd_to_15)
