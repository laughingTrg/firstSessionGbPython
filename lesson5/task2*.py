def odd_nums(max_num):                                              # создаем функцию для вывода нечетных чисел от 1 до n
    return (num for num in range(1, max_num + 1, 2))                # не используем yield, а return

odd_to_15 = odd_nums(15)                                            # запускаем функцию и присваиваем переменной генератор

while True:                                                         # проверяем работу функции до ошибки StopIteration
    print(next(odd_to_15))
