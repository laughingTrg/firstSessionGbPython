import json

with open('users.csv', 'r', encoding='utf-8') as file:      # получаем список строк пользователей
    user_data = file.readlines()
with open('hobby.csv', 'r', encoding='utf-8') as file:      # получем списко строк хобби
    hobby_data = file.readlines()

dict_user = {}                                              # создаем выходной словарь
if len(user_data) > len(hobby_data):                        # если длина списка строк пользователей больше
    for i in range(len(hobby_data)):                        # записываем данные с хобби
        dict_user[user_data[i].strip()] = hobby_data[i].strip()
    for i in range(len(hobby_data), len(user_data)):        # затем дописываем данные без хобби
        dict_user[user_data[i].strip()] = None
elif len(user_data) < len(hobby_data):                      # если длина меньше выходим с кодом "1"
    exit(1)
else:                                                       # если равны, то все заносим
    for i in range(len(user_data)):
        dict_user[user_data[i].strip()] = hobby_data[i].strip()

with open('dict_user.txt', 'w+', encoding='utf-8') as file: # записываем в файл
    file.write(json.dumps(dict_user))

with open('dict_user.txt', 'r+', encoding='utf-8') as file: # проверяем запись
    in_data = json.loads(file.read())
    print(in_data)