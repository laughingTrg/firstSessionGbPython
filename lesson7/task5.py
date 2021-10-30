import os
from collections import defaultdict

SIZE_100 = 10 ** 2                                                              # задаем константы размеров файлов
SIZE_1000 = 10 ** 3
SIZE_10000 = 10 ** 4
SIZE_100000 = 10 ** 5

root_dir = '.'                                                                  # указываем папку для поиска
out_dict = defaultdict(list)                                                    # задаем словарь для хранения файлов по размеру
res_dict = {}                                                                   # словарь результат

for root, dirs, files in os.walk(root_dir):                                     # рекурсивно проходимся по папкам
    for file in files:                                                          # выбираем каждый файл и сравниваем его размер с заданными константами
        if os.stat(os.path.join(root, file)).st_size < SIZE_100:                # если он соответсвует то к соответствующему ключу добавляем этот файл
            out_dict[SIZE_100].append(file)
        elif SIZE_100 < os.stat(os.path.join(root, file)).st_size < SIZE_1000:
            out_dict[SIZE_1000].append(file)
        elif SIZE_1000 < os.stat(os.path.join(root, file)).st_size < SIZE_10000:
            out_dict[SIZE_10000].append(file)
        elif SIZE_10000 < os.stat(os.path.join(root, file)).st_size < SIZE_100000:
            out_dict[SIZE_100000].append(file)

for key, values in out_dict.items():                                            # проходим по полученному словарю и выбираем из него пару ключ значение
    ext_values = []                                                             # создаем словарь для хранения расширенйи файлов
    for value in values:                                                        # проходим по каждому файлу и получаем из него расширение
        if value.rsplit('.', maxsplit=1)[-1] not in ext_values:                 # если его нет в списке расширений, добавляем
            ext_values.append(value.rsplit('.', maxsplit=1)[-1])
    res_dict[key] = (len(out_dict[key]), ext_values)                            # вносим информацию ключ - размер файлов, значение - количество и расщирения
print(res_dict.items())                                                         # выводим результат