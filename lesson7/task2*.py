'''
Образец структуры файла представлен ниже, суть в том, что уровень вложенности в дереве соответствует количеству '|' в строке с конфигурацией
...
|   |  |--models.py
|   |  |--views.py
|   |  |--templates
|   |  |   |--mainapp
|   |  |   |   |--base.html
|   |  |   |   |--index.html
...
'''
import os

def get_path(path_level, path_dict):                                                        # функция возвращает путь по заданному уровню вложенности и словарю папок
    out_path = []
    for i in range(path_level):
        out_path.append(path_dict[i][-1])
    return '/'.join(out_path)                                                               # из элементов списка получаем путь как строку

with open('config.yaml', 'r+', encoding='utf-8') as config:                                 # открываем файл для чтения
    dirs = {}                                                                               # словарь содержит уровни вложенности и папки в них
    for line in config:                                                                     # построчно читаем файл
        if (line.strip()[:line.strip().rfind('|--')].count('|')) < 1:                       # если уровень вложенности первый
            root_dir = line.strip()[3:]                                                     # получаем зазвание папки и добавляем в словарь
            dirs[0] = [root_dir]
            if not os.path.exists(root_dir):                                                # если папки не существует, создаем
                os.mkdir(root_dir)
        else:                                                                               # если не верхний уровень вложенности
            sub_level = (line.strip()[:line.strip().rfind('|--')].count('|'))               # определяем уровень вложенности элемента
            if sub_level not in dirs:                                                       # если ключа с уровнем нет создаем его
                dirs[sub_level] = []
            dir_path = get_path(sub_level, dirs)                                            # получаем путь до элемента конфига
            element = line.strip()[line.strip().rfind('|--') + 3:]                          # получаем сам элемент
            if element.find('.') == -1:                                                     # если это папка, без расширения
                if not os.path.exists(os.path.join(dir_path, element)):                     # если она не создана, создаем ее
                    os.makedirs(os.path.join(dir_path, element))
                dirs[sub_level].append(element)                                             # добавляем элемент в словарь
            else:                                                                           # если элемент - файл, с расширением
                if not os.path.exists(os.path.join(dir_path, element)):                     # если файл не создан создаем его и закрываем
                    f = open(os.path.join(dir_path, element), 'w', encoding='utf-8')
                    f.close()