import sys

sale = sys.argv[1]                  # получаем новое значение

with open('bakery.csv', 'a+', encoding='utf-8') as file: # добавляем новое значение в файл записей
    file.write(f'{sale}\n')