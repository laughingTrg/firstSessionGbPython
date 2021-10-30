import os
from collections import defaultdict

SIZE_100 = 10 ** 2                                                                      # задаем константы для размеров файлов
SIZE_1000 = 10 ** 3
SIZE_10000 = 10 ** 4
SIZE_100000 = 10 ** 5

root_dir = '.'                                                                          # задаем папку для рекурсивного поиска
out_dict = defaultdict(list)                                                            # создаем промежуточный и выходной словарь
res_dict = {}

for root, dirs, files in os.walk(root_dir):                                             # проходим по папкам и получаем файлы, папки и путь
    for file in files:                                                                  # проходим по файлу в файлах
        if os.stat(os.path.join(root, file)).st_size < SIZE_100:                        # если размер файла соответсвует заданным значениям
            out_dict[SIZE_100].append(file)                                             # добавляем в промежуточный словарь этот файл, ключ - размер
        elif SIZE_100 < os.stat(os.path.join(root, file)).st_size < SIZE_1000:
            out_dict[SIZE_1000].append(file)
        elif SIZE_1000 < os.stat(os.path.join(root, file)).st_size < SIZE_10000:
            out_dict[SIZE_10000].append(file)
        elif SIZE_10000 < os.stat(os.path.join(root, file)).st_size < SIZE_100000:
            out_dict[SIZE_100000].append(file)

for key in out_dict:                                                                    # проходим по ключам в промежуточном словаре
    res_dict[key] = len(out_dict[key])                                                  # и в выходной словарь добавляем количество файлов по ключу
print(res_dict)                                                                         # выводим результат