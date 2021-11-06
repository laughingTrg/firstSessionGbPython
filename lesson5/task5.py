import sys                                                                          # импортируем библиотеки
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]                               # создаем исходные данные


print('------------Без оптимизации------------')                                    # создаем решение в лоб через цикл for
start = perf_counter()                                                              # старт учета времени
res = []
for i in src:
    if src.count(i) < 2:                                                            # если количество элементов в исходном списке меньше 2
        res.append(i)                                                               # добавляем в список результата
stop = perf_counter()                                                               # старт учета времени

print(res, 'time=', stop - start, 'size=', sys.getsizeof(res))                      # вывод результата с временем выполнения и размером

print('------------Оптимизация по скорости------------')                            # создаем решение с оптимизацией по скорости
vopt_start = perf_counter()                                                         # старт учета времени
vopt_result = [num for num in src if src.count(num) < 2]                            # создаем List Comprehensions
vopt_stop = perf_counter()                                                          # старт учета времени

print(vopt_result, 'time=', vopt_stop - vopt_start, 'size=', sys.getsizeof(vopt_result))    # снижаем скорость, но размер т.к. на выходе список - размер такой же

print('------------Оптимизация по памяти------------')                              # создаем решение с оптимизацией по памяти
mopt_start = perf_counter()                                                         # старт учета времени
mopt_result = (num for num in src if src.count(num) < 2)                            # создаем генератор
mopt_stop = perf_counter()                                                          # конец учета времени

print(list(mopt_result), 'time=', mopt_stop - mopt_start, 'size=', sys.getsizeof(mopt_result))  # снижаем память, т.к. генератор весит меньше чем список
