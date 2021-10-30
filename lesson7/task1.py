import os

ROOT_DIR = 'my_projects'                                                    # задаем папку рут
IN_DIR = ['settings', 'mainapp', 'adminapp', 'authapp']                     # задаем папки входящие в папку рут

if not os.path.exists(ROOT_DIR):                                            # если папки рут нет - создаем
    os.mkdir(ROOT_DIR)
    for dir in IN_DIR:                                                      # проходим по списку папок, если их нет, создаем
        if not os.path.exists(os.path.join(ROOT_DIR, dir)):
            os.makedirs(os.path.join(ROOT_DIR, dir))



print(os.listdir(os.path.join(os.getcwd(), ROOT_DIR)))                      # покахываем список созданных папок в рут