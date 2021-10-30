import os
from shutil import copy

scan_dir = 'my_project'                                                                         # выбираем папку для сканирования
get_dir = 'templates'                                                                           # вводим папку куда переносим данные
out_list = [(root, dirs, files) for root, dirs, files in os.walk(scan_dir) if get_dir in root]  # создаем список путей, папок и фалов, которые
                                                                                                # есть в папках templates
if not os.path.exists(os.path.join(scan_dir, get_dir)):                                         # если папка не создана создаем ее в нужном месте
    os.mkdir(os.path.join(scan_dir, get_dir))
for element in out_list:                                                                        # проходим по полученному списку после сканирования
    if len(element[1]) > 0:                                                                     # если папки есть
        for i in range(len(element[1])):                                                        # создаем их если их нет в месте назначения
            if not os.path.exists(os.path.join(scan_dir, get_dir, element[1][i])):
                os.makedirs(os.path.join(scan_dir, get_dir, element[1][i]))
    if len(element[2]) > 0:                                                                     # если есть файлы копируем, если они не были скопированы ранее
        for i in element[2]:
            if not os.path.exists(os.path.join(scan_dir, get_dir, element[0].split(get_dir)[-1][1:], i)):
                copy(os.path.join(element[0], i), os.path.join(scan_dir, get_dir, element[0].split(get_dir)[-1][1:], i))
