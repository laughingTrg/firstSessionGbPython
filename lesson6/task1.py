f_obj = open('nginx_logs.txt', 'r', encoding='utf-8')   # получаем кортежи записей
out_list = [(line.split()[0], line.split()[5][1:], line.split()[6]) for line in f_obj]
f_obj.close()
print(out_list[:10])                                    # выводим 10 штук для примера