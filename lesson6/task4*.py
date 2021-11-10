import json

dict_user = {}                                                  # создаем выходной словарь
with open('users.csv', 'r', encoding='utf-8') as f_u:           # открываем файлы с пользователями и хобби
    with open('hobby.csv', 'r', encoding='utf-8') as f_h:
        user = f_u.readline().strip()                           # получаем первые строки файлов
        hobby = f_h.readline().strip()
        user_num = 0                                            # задаем номер пользователя
        while user and hobby:                                   # пока строки есть в обоих файлах
            user_info = {}                                      # создаем словарь пользователя
            user_info['Name'] = user.split(',')                 # помещаем туда список ФИО и хобби
            user_info['Hobby'] = hobby.split(',')
            dict_user[f'Пользователь {user_num + 1}'] = user_info   # заносим в выходной словарь
            user_num += 1                                       # инкрементируем пользователя и снова
            user = f_u.readline().strip()                       # получаем строки файлов
            hobby = f_h.readline().strip()
        while user:                                             # пока есть строки в ФИО
            user_info = {}                                      # добавляем в выходной словарь пользователя
            user_info['Name'] = (user.split(','))               # с списком ФИО и без хобби (None)
            user_info['Hobby'] = None
            dict_user[f'Пользователь {user_num + 1}'] = user_info
            user_num += 1
            user = f_u.readline().strip()
        while hobby:                                            # если только хобби выходим с кодом "1"
            exit(1)

with open('dict_user_task4.txt', 'w+', encoding='utf-8') as file:
    file.write(json.dumps(dict_user))

with open('dict_user_task4.txt', 'r+', encoding='utf-8') as file:
    in_data = json.loads(file.read())
    print(in_data)