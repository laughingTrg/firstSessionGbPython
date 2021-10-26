import json
import sys

user_file, hobby_file, out_dict = sys.argv[1:]          # получаем входные данные о расположении файлов

dict_user = {}                                          # создаем словарь для вывода
with open(user_file, 'r', encoding='utf-8') as f_u:     # открываем файлы исходников для работы
    with open(hobby_file, 'r', encoding='utf-8') as f_h:
        user = f_u.readline().strip()                   # сохраняем 1 строку файлов в соответствующие
        hobby = f_h.readline().strip()                  # переменные
        user_num = 0                                    # задаем переменную с номером пользователя
        while user and hobby:                           # пока количество записей в файлах равно
            user_info = {}                              # задаем словарь для каждого пользователя
            user_info['Name'] = user.split(',')         # задаем значения для ключей словаря имя и хобби
            user_info['Hobby'] = hobby.split(',')       # значения берем из соответсвуюзих строк файла
            dict_user[f'Пользователь {user_num + 1}'] = user_info   # итог заносим в выходной словарь
            user_num += 1                               # переходим к следующему пользователю
            user = f_u.readline().strip()               # получаем новые строки файлов
            hobby = f_h.readline().strip()              # исходных данных с именами и хобби
        while user:                                     # пока есть запись в файле с пользователями
            user_info = {}                              # создаем нового пользователя только с ФИО
            user_info['Name'] = (user.split(','))       # в ключе хобби присваиваем None
            user_info['Hobby'] = None
            dict_user[f'Пользователь {user_num + 1}'] = user_info
            user_num += 1
            user = f_u.readline().strip()
        while hobby:                                    # если остались только записи с хобби
            exit(1)                                     # выходим с кодом "1"

with open(out_dict, 'w+', encoding='utf-8') as file:    # если с записями все хорошо
    file.write(json.dumps(dict_user))                   # записываем выхожной словарь

with open(out_dict, 'r+', encoding='utf-8') as file:    # првоеряем, что записано верно
    in_data = json.loads(file.read())
    print(in_data)