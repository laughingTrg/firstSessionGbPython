import sys

number = int(sys.argv[1])                               # получаем данные о записи и значении
value = sys.argv[2]
is_number = False                                       # переменная проверяет есть ли такая запись

with open('bakery.csv', 'r+', encoding='utf-8') as file:    # открываем исхлжный файл
    with open('bakery_edit.csv', 'w+', encoding='utf-8') as f_edit: # открываем файл для изменений

        for num, line in enumerate(file):               # проходим по исходному файлу
            if num < number - 1:                        # пока заданная запись меньше на 1 чем текущая
                f_edit.write(line)                      # записываем в файл изменений
            elif num == number - 1:                     # если запись равна заданной
                is_number = True                        # устанавливаем флаг наличия записи
                f_edit.write(value + '\n')              # записываем новое значение
            else:                                       # записываем остальные записи
                f_edit.write(line)
        if is_number == False:                          # если записи заданной не было, выходим с текстом
            print('Такой записи не существует')

if is_number:                                                       # если запись была, открываем файл
    with open('bakery.csv', 'w+', encoding='utf-8') as file:        # с записями на редактирование
        with open('bakery_edit.csv', 'r+', encoding='utf-8') as f_edit:
            for line in f_edit:                                     # и переписываем измененные данные
                file.write(line)                                    # в исходный файл
